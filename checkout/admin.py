from decimal import Decimal
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)
    fields = ("product", "option", "quantity", "lineitem_total")
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ("order_number", "date", "delivery_cost", "order_total", "grand_total")

    fields = (
        "order_number",
        "date",
        "full_name",
        "email",
        "phone_number",
        "street_address1",
        "street_address2",
        "town_or_city",
        "county",
        "country",
        "postcode",
        "delivery_cost",
        "order_total",
        "grand_total",
    )

    list_display = ("order_number", "full_name", "date", "order_total", "delivery_cost", "grand_total")
    ordering = ("-date",)

    def save_model(self, request, obj, form, change):
        """
        When adding a new Order in admin, it must have NOT NULL totals.
        Set them to 0.00 so the initial save succeeds.
        We'll recalc after inlines are saved.
        """
        if not obj.pk:
            obj.order_total = obj.order_total or Decimal("0.00")
            obj.delivery_cost = obj.delivery_cost or Decimal("0.00")
            obj.grand_total = obj.grand_total or Decimal("0.00")
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        """
        After inline OrderLineItems are saved, compute totals properly.
        """
        super().save_related(request, form, formsets, change)
        form.instance.update_total()


admin.site.register(Order, OrderAdmin)
