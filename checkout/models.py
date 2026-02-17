from decimal import Decimal
from django.db import models
from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from products.models import Product
import uuid

# Create your models here.

class Order(models.Model):
    order_number = models.CharField(max_length=32, unique=True, editable=False)
    user_profile = models.ForeignKey(
    "profiles.UserProfile",
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="orders",
)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    street_address1 = models.CharField(max_length=80)
    street_address2 = models.CharField(max_length=80, blank=True)
    town_or_city = models.CharField(max_length=40)
    county = models.CharField(max_length=80, blank=True)
    country = CountryField(blank_label="Select Country (optional)", null=False, blank=False)
    postcode = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, default=Decimal("0.00"))
    order_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal("0.00"))
    original_bag = models.TextField(null=False, blank=False, default="")
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default="")
    save_info = models.BooleanField(default=False)
    confirmation_email_sent = models.BooleanField(default=False)

    def _generate_order_number(self):
        """ Generate a random, unique order number using UUID """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """ Update total each time a line item is added, accounting for delivery costs """
        self.order_total = sum(item.lineitem_total for item in self.lineitems.all()) or Decimal("0.00")
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        else:
            self.delivery_cost = Decimal("0.00")
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """ Override the original save method to set the order number if it hasn't been set already """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    OPTION_SINGLE = "single"
    OPTION_SET = "set"

    OPTION_CHOICES = (
        (OPTION_SINGLE, "Single Item or Single D20"),
        (OPTION_SET, "Full dice set of 7"),
    )

    order = models.ForeignKey(
        "checkout.Order",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="lineitems",
    )
    product = models.ForeignKey(
        "products.Product",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )

    option = models.CharField(
        max_length=10,
        choices=OPTION_CHOICES,
        default=OPTION_SINGLE,
    )

    quantity = models.IntegerField(null=False, blank=False)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    
    def save(self, *args, **kwargs):
        """Set lineitem total and update order total."""
        
        # If quantity is 0 (or less), delete the line item instead of saving it
        if self.quantity <= 0:
            if self.pk:
                self.delete()
                self.order.update_total()
            return
        # If the product doesn't support a set price, force SINGLE
        if not self.product.dice_set_price:
            self.option = self.OPTION_SINGLE

        # Pick the right unit price
        if self.option == self.OPTION_SET and self.product.dice_set_price is not None:
            unit_price = self.product.dice_set_price
        else:
            unit_price = self.product.price
        # Safety: if price is missing, don't crash silently
        if unit_price is None:
            unit_price = 0

        self.lineitem_total = unit_price * self.quantity
        super().save(*args, **kwargs)
        self.order.update_total()
       