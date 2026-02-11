# checkout/views.py

import stripe
from decimal import Decimal

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, get_object_or_404

from bag.contexts import bag_contents
from products.models import Product
from .forms import OrderForm
from .models import OrderLineItem, Order


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
            order.order_total = current_bag["total"]
            order.delivery_cost = current_bag["delivery"]
            order.grand_total = current_bag["grand_total"]

            payment_intent_id = request.POST.get("payment_intent_id", "")
            if hasattr(order, "stripe_pid"):
                order.stripe_pid = payment_intent_id

            order.save()

            for item_key, item_data in bag.items():
                if ":" in str(item_key) and isinstance(item_data, int):
                    item_id, option = str(item_key).split(":", 1)
                    try:
                        product = Product.objects.get(id=int(item_id))
                    except Product.DoesNotExist:
                        messages.error(request, "A product in your bag wasn't found. Please try again.")
                        order.delete()
                        return redirect(reverse("view_bag"))

                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        option=option,
                        quantity=item_data,
                    )
                    continue

                try:
                    product = Product.objects.get(id=int(item_key))
                except (ValueError, TypeError, Product.DoesNotExist):
                    messages.error(request, "A product in your bag wasn't found. Please try again.")
                    order.delete()
                    return redirect(reverse("view_bag"))

                # B1: simple quantity
                if isinstance(item_data, int):
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        option="single",   
                        quantity=item_data,
                    )
                else:
                    items_by_option = item_data.get("items_by_option", {})
                    for option, quantity in items_by_option.items():
                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            option=option,
                            quantity=quantity,
                        )
            order.update_total()

            request.session["bag"] = {}
            return redirect(reverse("order_confirmation", args=[order.order_number]))

        messages.error(request, "There was an error with your form. Please check your details.")

    current_bag = bag_contents(request)
    grand_total = Decimal(str(current_bag["grand_total"]))
    amount = int((grand_total * Decimal("100")).to_integral_value())  # pounds -> pence

    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=settings.STRIPE_CURRENCY,
        metadata={"bag": str(bag)},
    )

    if not settings.STRIPE_PUBLIC_KEY:
        messages.warning(request, "Stripe public key is missing. Check your environment variables.")

    context = {
        "order_form": OrderForm(),
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY,
        "client_secret": intent.client_secret,
    }
    return render(request, "checkout/checkout.html", context)


def order_confirmation(request, order_number):
    save_info = request.session.get("save_info", False)
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f"Order successfully processed! Your order number is {order_number}.")

    if "bag" in request.session:
        del request.session["bag"]
    
    template = "checkout/order_confirmation.html"
    context = {
        "order": order,
    }

    return render(request, template, context)