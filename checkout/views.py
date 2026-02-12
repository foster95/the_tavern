# checkout/views.py

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


@require_POST
def cache_checkout_data(request):
    """
    CI-style: store bag + prefs on the PaymentIntent metadata before confirming payment.
    Called from JS.
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
                "username": request.user.get_username() if request.user.is_authenticated else "anonymous",
            },
        )
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be processed right now. Please try again later."
        )
        return HttpResponse(content=str(e), status=400)


def checkout(request):
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(request, "Your bag is empty. Please add items before checking out.")
        return redirect(reverse("products"))

    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        order_form = OrderForm(request.POST)

        if order_form.is_valid():
            order = order_form.save(commit=False)

            current_bag = bag_contents(request)
            order.order_total = current_bag.get("total", Decimal("0.00"))
            order.delivery_cost = current_bag.get("delivery", Decimal("0.00"))
            order.grand_total = current_bag.get("grand_total", order.order_total + order.delivery_cost)

            client_secret = request.POST.get("client_secret", "")
            if not client_secret or "_secret" not in client_secret:
                messages.error(request, "Missing Stripe client secret. Please try again.")
                return redirect(reverse("checkout"))

            pid = client_secret.split("_secret")[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)

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

            request.session["bag"] = {}
            return redirect(reverse("order_confirmation", args=[order.order_number]))

        messages.error(request, "There was an error with your form. Please check your details.")

    current_bag = bag_contents(request)
    grand_total = Decimal(str(current_bag.get("grand_total", Decimal("0.00"))))
    amount = int((grand_total * Decimal("100")).to_integral_value())  # pounds -> pence

    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=settings.STRIPE_CURRENCY,
        metadata={"bag": json.dumps(bag)},
    )

    if not settings.STRIPE_PUBLIC_KEY:
        messages.warning(request, "Stripe public key is missing. Check your environment variables.")

    context = {
        "order_form": OrderForm(request.POST or None),
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        "client_secret": intent.client_secret,
    }
    return render(request, "checkout/checkout.html", context)


def order_confirmation(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f"Order successfully processed! Your order number is {order_number[:12]}.")

    if "bag" in request.session:
        del request.session["bag"]

    return render(request, "checkout/order_confirmation.html", {"order": order})
