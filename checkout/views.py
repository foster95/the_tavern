import json
from decimal import Decimal
import stripe
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.http import require_POST
from bag.contexts import bag_contents
from products.models import Product
from .forms import OrderForm
from .models import Order, OrderLineItem
from profiles.models import UserProfile
from profiles.forms import UserProfileForm


@require_POST
def cache_checkout_data(request):
    """
    Store bag + prefs on the PaymentIntent metadata before confirming payment.
    """
    try:
        client_secret = request.POST.get("client_secret", "")
        pid = client_secret.split("_secret")[0]

        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "bag": json.dumps(request.session.get("bag", {})),
                "save_info": request.POST.get("save_info", "false"),
                "username": (
                    request.user.get_username()
                    if request.user.is_authenticated
                    else "anonymous"
                ),
            },
        )
        request.session["save_info"] = request.POST.get("save_info", "false")
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request,
            (
                "Sorry, your payment cannot be processed right now. "
                "Please try again later."
            )
        )
        return HttpResponse(content=str(e), status=400)


def checkout(request):
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(
            request,
            "Your bag is empty. Please add items before checking out.")
        return redirect(reverse("products"))

    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order = order_form.save(commit=False)

            current_bag = bag_contents(request)
            order.order_total = current_bag.get("total", Decimal("0.00"))
            order.delivery_cost = current_bag.get("delivery", Decimal("0.00"))
            order.grand_total = current_bag.get(
                "grand_total", order.order_total + order.delivery_cost)

            client_secret = request.POST.get("client_secret", "")
            if not client_secret or "_secret" not in client_secret:
                messages.error(
                    request, "Missing Stripe client secret. Please try again.")
                return redirect(reverse("checkout"))

            order.save_info = (
                request.POST.get("save_info", "false") == "true")
            pid = client_secret.split("_secret")[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)

            try:
                stripe.PaymentIntent.modify(
                    pid,
                    receipt_email=(order.email or "").strip(),  # <-- key line
                    )
            except Exception:
                pass

            order.save()

            for item_key, item_data in bag.items():
                if ":" in str(item_key) and isinstance(item_data, int):
                    item_id, option = str(item_key).split(":", 1)
                    product = get_object_or_404(Product, id=int(item_id))

                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        option=option.strip().lower(),
                        quantity=item_data,
                    )
                    continue

                product = get_object_or_404(Product, id=int(item_key))

                if isinstance(item_data, int):
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        option=OrderLineItem.OPTION_SINGLE,
                        quantity=item_data,
                    )
                else:
                    items_by_option = item_data.get("items_by_option", {})
                    for option, quantity in items_by_option.items():
                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            option=(option or "").strip().lower(),
                            quantity=quantity,
                        )

            order.update_total()

            return redirect(reverse(
                "order_confirmation", args=[order.order_number]))

        messages.error(
            request, (
                "There was an error with your form. Please check your details."
                )
            )

    current_bag = bag_contents(request)
    grand_total = Decimal(str(current_bag.get("grand_total", Decimal("0.00"))))
    amount = int((grand_total * Decimal("100")).to_integral_value())

    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=settings.STRIPE_CURRENCY,
        metadata={"bag": json.dumps(bag)},
    )

    if request.user.is_authenticated:
        profile, _ = UserProfile.objects.get_or_create(user=request.user)

        order_form = OrderForm(initial={
            "first_name": profile.default_first_name or "",
            "last_name": profile.default_last_name or "",
            "email": request.user.email or "",
            "phone_number": profile.default_phone_number or "",
            "street_address1": profile.default_street_address1 or "",
            "street_address2": profile.default_street_address2 or "",
            "town_or_city": profile.default_town_or_city or "",
            "county": profile.default_county or "",
            "postcode": profile.default_postcode or "",
            "country": profile.default_country or "",
        })
    else:
        order_form = OrderForm()

    if not settings.STRIPE_PUBLIC_KEY:
        messages.warning(
            request,
            (
                "Stripe public key is missing."
                "Check your environment variables."
            ),
        )

    context = {
        "order_form": order_form,
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        "client_secret": intent.client_secret,
    }
    return render(request, "checkout/checkout.html", context)


def order_confirmation(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    if "bag" in request.session:
        del request.session["bag"]

    if request.user.is_authenticated:
        profile, _ = UserProfile.objects.get_or_create(user=request.user)

        if order.user_profile_id != profile.id:
            order.user_profile = profile
            order.save(update_fields=["user_profile"])

        save_info = request.session.get("save_info", "false")
        save_info_truthy = str(save_info).lower() in ("true", "1", "on", "yes")

        if save_info_truthy:
            profile_data = {
                "default_first_name": order.first_name,
                "default_last_name": order.last_name,
                "default_phone_number": order.phone_number,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_town_or_city": order.town_or_city,
                "default_county": order.county,
                "default_postcode": order.postcode,
                "default_country": order.country,
            }

            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
                messages.success(
                    request, "Saved your delivery info for next time.")
            else:
                print(user_profile_form.errors)
                messages.warning(
                    request,
                    (
                        "We couldn't save your delivery info automatically."
                        "You can update it in your profile."
                    ),
                )

    messages.success(
        request,
        (
            "Order successfully processed!"
            f"Your order number is {order_number[:12]}."
        ),
    )

    return render(request, "checkout/order_confirmation.html",
                  {"order": order,
                   })
