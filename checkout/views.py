# checkout/views.py

import stripe
from decimal import Decimal

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404

from bag.contexts import bag_contents
from products.models import Product

from .forms import OrderForm
from .models import OrderLineItem


def checkout(request):
    bag = request.session.get("bag", {})
    if not bag:
        messages.error(request, "Your bag is empty. Please add items before checking out.")
        return redirect(reverse("products"))

    stripe.api_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        form = OrderForm(request.POST)

        if form.is_valid():
            order = form.save(commit=False)

            current_bag = bag_contents(request)
            order.order_total = current_bag["total"]
            order.delivery_cost = current_bag["delivery"]
            order.grand_total = current_bag["grand_total"]

            payment_intent_id = request.POST.get("payment_intent_id", "")
            print("🔥 POST received. payment_intent_id =", payment_intent_id)

            if hasattr(order, "stripe_pid"):
                order.stripe_pid = payment_intent_id

            order.save()

            for item_id, item_data in bag.items():
                product = get_object_or_404(Product, pk=item_id)

                if isinstance(item_data, dict) and "items_by_option" in item_data:
                    for option, quantity in item_data["items_by_option"].items():
                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            option=option,
                            quantity=quantity,
                        )
                else:
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        quantity=item_data,
                    )

            order.update_total()

            request.session["bag"] = {}

            messages.success(request, "Payment successful! Order placed.")
            return redirect(reverse("products"))

        messages.error(request, "There was an error with your form. Please check your details.")

    current_bag = bag_contents(request)
    grand_total = Decimal(str(current_bag["grand_total"]))
    amount = int((grand_total * Decimal("100")).to_integral_value())  # pounds -> pence

    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=settings.STRIPE_CURRENCY,
        metadata={"bag": str(bag)},
    )

    print(intent)

    form = OrderForm()

    if not settings.STRIPE_PUBLIC_KEY:
        messages.warning(request, "Stripe public key is missing. Check your environment variables.")

    context = {
        "order_form": form,
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        "client_secret": intent.client_secret,
    }
    return render(request, "checkout/checkout.html", context)
