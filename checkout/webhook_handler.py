import json
import time
from decimal import Decimal

import stripe
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from products.models import Product
from .models import Order, OrderLineItem


class StripeWebhookHandler:
    """Handle Stripe webhooks."""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic/unknown webhook event."""
        return HttpResponse(content=f"Webhook received: {event['type']}", status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe.
        If an order already exists for this PaymentIntent (stripe_pid), do nothing.
        Otherwise create it (fallback).
        """
        stripe.api_key = settings.STRIPE_SECRET_KEY

        intent = event.data.object
        pid = intent.id  

        metadata = getattr(intent, "metadata", {}) or {}
        bag = metadata.get("bag", "{}")
        save_info = metadata.get("save_info", "false")  

        order = None

        try:
            stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
            billing_details = stripe_charge.billing_details

            billing_email = getattr(billing_details, "email", "") or ""

            shipping_details = getattr(intent, "shipping", None) or {}
            shipping_address = getattr(shipping_details, "address", None) or {}
            stripe_total = Decimal(str(stripe_charge.amount)) / Decimal("100")

            for attr in ("line2", "state", "postal_code"):
                try:
                    if getattr(shipping_address, attr, None) == "":
                        setattr(shipping_address, attr, None)
                except Exception:
                    pass

            try:
                bag_dict = json.loads(bag)
            except json.JSONDecodeError:
                bag_dict = json.loads(bag.replace("'", '"'))

            attempt = 1
            while attempt <= 10:
                order = Order.objects.filter(stripe_pid=pid).first()
                if order:
                    return HttpResponse(
                        content=f"Webhook received: {event['type']} | SUCCESS: Order already exists in database",
                        status=200,
                    )
                attempt += 1
                time.sleep(1)

            order = Order.objects.create(
                first_name=(getattr(shipping_details, "first_name", "") or ""),
                last_name=(getattr(shipping_details, "last_name", "") or ""),
                email=billing_email,
                phone_number=(getattr(shipping_details, "phone", "") or ""),
                street_address1=(getattr(shipping_address, "line1", "") or ""),
                street_address2=(getattr(shipping_address, "line2", "") or "") or "",
                town_or_city=(getattr(shipping_address, "city", "") or ""),
                county=(getattr(shipping_address, "state", "") or "") or "",
                country=(getattr(shipping_address, "country", "") or ""),
                postcode=(getattr(shipping_address, "postal_code", "") or "") or "",
                order_total=Decimal("0.00"),
                delivery_cost=Decimal("0.00"),
                grand_total=Decimal("0.00"),
                original_bag=bag,
                stripe_pid=pid,
            )

            for item_key, item_data in bag_dict.items():
                if ":" in str(item_key) and isinstance(item_data, int):
                    item_id, option = str(item_key).split(":", 1)
                    product = get_object_or_404(Product, id=int(item_id))

                    option = (option or "").strip().lower()
                    if option not in (OrderLineItem.OPTION_SINGLE, OrderLineItem.OPTION_SET):
                        option = OrderLineItem.OPTION_SINGLE

                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        option=option,
                        quantity=item_data,
                        lineitem_total=Decimal("0.00"),
                    )
                    continue
                product = get_object_or_404(Product, id=int(item_key))

                if isinstance(item_data, int):
                    OrderLineItem.objects.create(
                        order=order,
                        product=product,
                        option=OrderLineItem.OPTION_SINGLE,
                        quantity=item_data,
                        lineitem_total=Decimal("0.00"),
                    )
                else:
                    for option, quantity in item_data.get("items_by_option", {}).items():
                        option = (option or "").strip().lower()
                        if option not in (OrderLineItem.OPTION_SINGLE, OrderLineItem.OPTION_SET):
                            option = OrderLineItem.OPTION_SINGLE

                        OrderLineItem.objects.create(
                            order=order,
                            product=product,
                            option=option,
                            quantity=quantity,
                            lineitem_total=Decimal("0.00"),
                        )

            order.update_total()

            return HttpResponse(
                content=f"Webhook received: {event['type']} | SUCCESS: Order created by webhook (not found after 10 attempt(s))",
                status=200,
            )

        except Exception as e:
            if order:
                order.delete()
            return HttpResponse(
                content=f"Webhook received: {event['type']} | ERROR: {type(e).__name__}: {e}",
                status=500,
            )

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook."""
        return HttpResponse(content=f"Webhook received: {event['type']}", status=200)
