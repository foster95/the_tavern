from django.contrib import admin
from .models import Order, OrderLineItem

# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)
    fields = ("product", "option", "quantity", "lineitem_total")

    def get_readonly_fields(self, request, obj=None):
        if obj and not obj.product.dice_set_price:
            return self.readonly_fields + ("option",)
        return self.readonly_fields

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ( "order_number", "date",
                       "delivery_cost", "order_total", 
                       "grand_total",)
    
    fields = ( "order_number", "full_name", "email",
               "phone_number", "street_address1", "street_address2",
               "town_or_city", "county", "country", "postcode",
               "date", "delivery_cost", "order_total",
               "grand_total",)
    
    list_display = ("order_number", "full_name", "date",
                    "order_total", "delivery_cost", "grand_total",)
    
    ordering = ("-date",)

admin.site.register(Order, OrderAdmin)
