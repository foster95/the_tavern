# checkout/admin.py

from decimal import Decimal

from django import forms
from django.contrib import admin, messages

from .models import Order, OrderLineItem


class OrderLineItemInlineForm(forms.ModelForm):
    """
    Inline form validation:
    If someone selects "Full dice set of 7" for a product that has no set price
    (dice_set_price is None or 0.00), we auto-change it to SINGLE and remember
    the product name so the admin can show a warning message after save.
    """
    class Meta:
        model = OrderLineItem
        fields = "__all__"

    def clean(self):
        cleaned = super().clean()
        product = cleaned.get("product")
        option = cleaned.get("option")

        # Treat None OR 0.00 as "no set price"
        has_set_price = bool(product and product.dice_set_price)

        if product and option == OrderLineItem.OPTION_SET and not has_set_price:
            cleaned["option"] = OrderLineItem.OPTION_SINGLE
            # flag for admin messaging later
            self._corrected_to_single_name = product.name

        return cleaned


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    form = OrderLineItemInlineForm
    readonly_fields = ("lineitem_total",)
    fields = ("product", "option", "quantity", "lineitem_total")
    extra = 0
    can_delete = True


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
        When adding a new Order in admin, totals are NOT NULL in the DB.
        Set them to 0.00 so the first save succeeds.
        """
        if not obj.pk:
            obj.order_total = obj.order_total or Decimal("0.00")
            obj.delivery_cost = obj.delivery_cost or Decimal("0.00")
            obj.grand_total = obj.grand_total or Decimal("0.00")
        super().save_model(request, obj, form, change)

    def save_related(self, request, form, formsets, change):
        """
        After inline OrderLineItems are saved show warnings for any 
        auto-corrected "set" selections and recalculate order totals
        """
        super().save_related(request, form, formsets, change)

        corrected_products = []

        for fs in formsets:
            for inline_form in fs.forms:
                name = getattr(inline_form, "_corrected_to_single_name", None)
                if name:
                    corrected_products.append(name)

        for name in sorted(set(corrected_products)):
            messages.warning(
                request,
                f"{name} cannot be sold as part of a dice set. "
                "This item has been changed to 'Single Item or Single D20'."
            )

        form.instance.update_total()


admin.site.register(Order, OrderAdmin)
