import json
import time
from decimal import Decimal

import stripe
from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

from products.models import Product
from .models import Order, OrderLineItem
from profiles.models import UserProfile


class StripeWebhookHandler:
    """Handle Stripe webhooks."""

    def __init__(self, request):
        self.request = request

    def send_confirmation_email(self, order):
        if order.confirmation_email_sent:
            return
        
        customer_email = (order.email or "").strip()
        if not customer_email:
            return
        
        subject = render_to_string(
            "checkout/checkout_emails/order_confirmation_subject.txt",
            {"order": order},
            )
        subject = " ".join(subject.splitlines()).strip()
        
        body = render_to_string(
            "checkout/checkout_emails/order_confirmation_body.txt",
            {"order": order, "contact_email": settings.DEFAULT_FROM_EMAIL},
            )
        
        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [customer_email])
        
        order.confirmation_email_sent = True
        order.save(update_fields=["confirmation_email_sent"])




    def handle_event(self, event):
        """Handle a generic/unknown webhook event."""
        return HttpResponse(content=f"Webhook received: {event['type']}", status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook.

        Normal flow:
        - Your checkout view creates the Order already.
        - This webhook finds it and sends confirmation email.

        Fallback:
        - If no Order exists yet, create it from Stripe data + bag metadata.
        - Email address is taken from intent.receipt_email first (best), then charge billing email.
        """
        stripe.api_key = settings.STRIPE_SECRET_KEY

        intent = event.data.object
        pid = intent.id

        metadata = getattr(intent, "metadata", {}) or {}
        bag = metadata.get("bag", "{}")
        username = metadata.get("username", "anonymous")

        save_info = str(metadata.get("save_info", "false")).lower() in ("true", "1", "yes", "on")

        # 1) Prefer the email YOU set at checkout: PaymentIntent.receipt_email
        billing_email = (getattr(intent, "receipt_email", "") or "").strip()

        # 2) Stripe totals + optional email fallback from latest charge
        stripe_total = Decimal("0.00")
        try:
            latest_charge_id = getattr(intent, "latest_charge", None)
            if latest_charge_id:
                stripe_charge = stripe.Charge.retrieve(latest_charge_id)
                stripe_total = Decimal(str(stripe_charge.amount)) / Decimal("100")

                # Only use charge email if receipt_email was empty
                if not billing_email:
                    billing_details = getattr(stripe_charge, "billing_details", None)
                    if billing_details:
                        billing_email = (getattr(billing_details, "email", "") or "").strip()
        except Exception:
            # IMPORTANT: do not overwrite billing_email here
            pass

        # --- Shipping details on the PaymentIntent ---
        shipping = getattr(intent, "shipping", None)
        shipping_name = getattr(shipping, "name", "") if shipping else ""
        shipping_phone = getattr(shipping, "phone", "") if shipping else ""
        shipping_address = getattr(shipping, "address", None) if shipping else None

        line1 = getattr(shipping_address, "line1", "") if shipping_address else ""
        line2 = getattr(shipping_address, "line2", "") if shipping_address else ""
        city = getattr(shipping_address, "city", "") if shipping_address else ""
        state = getattr(shipping_address, "state", "") if shipping_address else ""
        postal_code = getattr(shipping_address, "postal_code", "") if shipping_address else ""
        country = getattr(shipping_address, "country", "") if shipping_address else ""

        # --- Parse bag JSON safely ---
        try:
            bag_dict = json.loads(bag) if isinstance(bag, str) else bag
        except json.JSONDecodeError:
            bag_dict = json.loads(str(bag).replace("'", '"'))

        # --- Get / update profile (only if user exists) ---
        profile = None
        if username != "anonymous":
            try:
                profile, _ = UserProfile.objects.get_or_create(user__username=username)
            except Exception:
                profile = None

            if profile and save_info:
                parts = (shipping_name or "").split()
                profile.default_first_name = parts[0] if parts else ""
                profile.default_last_name = " ".join(parts[1:]) if len(parts) > 1 else ""

                profile.default_phone_number = shipping_phone or ""
                profile.default_street_address1 = line1 or ""
                profile.default_street_address2 = line2 or ""
                profile.default_town_or_city = city or ""
                profile.default_county = state or ""
                profile.default_postcode = postal_code or ""
                profile.default_country = country or ""
                profile.save()

        # --- Give your normal checkout view a moment to write the Order ---
        for _ in range(10):
            existing = Order.objects.filter(stripe_pid=pid).first()
            if existing:
                # Optional safety: if order has no email but Stripe has one, fill it.
                if billing_email and not (existing.email or "").strip():
                    existing.email = billing_email
                    existing.save(update_fields=["email"])

                self.send_confirmation_email(existing)
                return HttpResponse(
                    content=f"Webhook received: {event['type']} | SUCCESS: Order already exists",
                    status=200,
                )
            time.sleep(1)

        # --- Fallback: create the Order if it still doesn't exist ---
        order = None
        try:
            name_parts = (shipping_name or "").split()
            first_name = name_parts[0] if name_parts else ""
            last_name = " ".join(name_parts[1:]) if len(name_parts) > 1 else ""

            order = Order.objects.create(
                user_profile=profile,
                first_name=first_name,
                last_name=last_name,
                email=billing_email,  # receipt_email preferred
                phone_number=shipping_phone or "",
                street_address1=line1 or "",
                street_address2=line2 or "",
                town_or_city=city or "",
                county=state or "",
                country=country or "",
                postcode=postal_code or "",
                order_total=Decimal("0.00"),
                delivery_cost=Decimal("0.00"),
                grand_total=Decimal("0.00"),
                original_bag=json.dumps(bag_dict),
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
                    items_by_option = item_data.get("items_by_option", {})
                    for option, quantity in items_by_option.items():
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

            self.send_confirmation_email(order)
            return HttpResponse(
                content=f"Webhook received: {event['type']} | SUCCESS: Order created by webhook fallback",
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
