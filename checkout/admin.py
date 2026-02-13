# checkout/admin.py

from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = (
        "order_number",
        "short_order_number",
        "date",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )

    fields = (
        "order_number",
        "short_order_number",
        "date",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "street_address1",
        "street_address2",
        "town_or_city",
        "county",
        "country",
        "postcode",
        "order_total",
        "delivery_cost",
        "grand_total",
        "original_bag",
        "stripe_pid",
    )

    list_display = (
        "short_order_number",
        "date",
        "first_name",
        "last_name",
        "order_total",
        "delivery_cost",
        "grand_total",
        "stripe_pid",
    )

    ordering = ("-date",)

    def short_order_number(self, obj):
        return obj.order_number[:12]

    short_order_number.short_description = "Order Number"
