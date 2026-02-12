# checkout/webhook_handler.py

import json
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
        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe.
        Only create an order if it doesn't already exist (CI style).
        """
        stripe.api_key = settings.STRIPE_SECRET_KEY

        intent = event.data.object
        pid = intent.id

        metadata = intent.metadata or {}
        bag = metadata.get("bag", "{}")
        save_info = metadata.get("save_info", "false")

        order = None

        try:
            # Retrieve charge & billing details
            stripe_charge = stripe.Charge.retrieve(intent.latest_charge)
            billing_details = stripe_charge.billing_details

            # Shipping info (sent from frontend)
            shipping_details = intent.shipping
            shipping_address = shipping_details.address

            # Stripe amount is in pence → pounds
            stripe_total = Decimal(str(stripe_charge.amount)) / Decimal("100")

            # Clean empty strings
            if shipping_address.line2 == "":
                shipping_address.line2 = None
            if shipping_address.state == "":
                shipping_address.state = None
            if shipping_address.postal_code == "":
                shipping_address.postal_code = None

            # Parse bag JSON
            try:
                bag_dict = json.loads(bag)
            except json.JSONDecodeError:
                bag_dict = json.loads(bag.replace("'", '"'))

            # Check if order already exists (CI-style match)
            order = Order.objects.get(
                full_name__iexact=(shipping_details.name or ""),
                email__iexact=(billing_details.get("email") or ""),
                phone_number__iexact=(shipping_details.phone or ""),
                street_address1__iexact=(shipping_address.line1 or ""),
                street_address2__iexact=(shipping_address.line2 or "") or "",
                town_or_city__iexact=(shipping_address.city or ""),
                county__iexact=(shipping_address.state or "") or "",
                country__iexact=(shipping_address.country or ""),
                postcode__iexact=(shipping_address.postal_code or "") or "",
                grand_total=stripe_total,
            )

            return HttpResponse(
                content=f"Webhook received: {event['type']} | SUCCESS: Order already exists",
                status=200,
            )

        except Order.DoesNotExist:
            # Create order
            try:
                order = Order.objects.create(
                    full_name=(shipping_details.name or ""),
                    email=(billing_details.get("email") or ""),
                    phone_number=(shipping_details.phone or ""),
                    street_address1=(shipping_address.line1 or ""),
                    street_address2=(shipping_address.line2 or "") or "",
                    town_or_city=(shipping_address.city or ""),
                    county=(shipping_address.state or "") or "",
                    country=(shipping_address.country or ""),
                    postcode=(shipping_address.postal_code or "") or "",
                    order_total=Decimal("0.00"),
                    delivery_cost=Decimal("0.00"),
                    grand_total=Decimal("0.00"),
                )

                # Create line items
                for item_key, item_data in bag_dict.items():
                    if ":" in str(item_key) and isinstance(item_data, int):
                        item_id, option = str(item_key).split(":", 1)
                        product = get_object_or_404(Product, id=int(item_id))

                        option = option.strip().lower()
                        if option not in (
                            OrderLineItem.OPTION_SINGLE,
                            OrderLineItem.OPTION_SET,
                        ):
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
                        for option, quantity in item_data.get(
                            "items_by_option", {}
                        ).items():
                            option = option.strip().lower()
                            if option not in (
                                OrderLineItem.OPTION_SINGLE,
                                OrderLineItem.OPTION_SET,
                            ):
                                option = OrderLineItem.OPTION_SINGLE

                            OrderLineItem.objects.create(
                                order=order,
                                product=product,
                                option=option,
                                quantity=quantity,
                                lineitem_total=Decimal("0.00"),
                            )

                order.update_total()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f"Webhook received: {event['type']} | ERROR: {e}",
                    status=500,
                )

        except Exception as e:
            return HttpResponse(
                content=f"Webhook received: {event['type']} | ERROR: {e}",
                status=500,
            )

        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        """Handle the payment_intent.payment_failed webhook."""
        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200,
        )
