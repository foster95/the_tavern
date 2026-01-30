from django.contrib import admin
import calendar
from .models import ProductOfTheMonth
from .models import Testimonial

@admin.register(ProductOfTheMonth)
class ProductOfTheMonthAdmin(admin.ModelAdmin):
    list_display = ("month_display", "year", "product")
    list_filter = ("year",)
    ordering = ("-year", "-month")

    def month_display(self, obj):
        """
        Display month as 'January', 'February', etc.
        Works even if old rows stored month as a string.
        """
        try:
            month_int = int(obj.month)
            return calendar.month_name[month_int]
        except (TypeError, ValueError, IndexError):
            return str(obj.month)

    month_display.short_description = "Month"

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("customer_display", "is_featured", "is_active", "sort_order", "created_at")
    list_filter = ("is_featured", "is_active")
    search_fields = ("quote", "customer_name", "name")  # harmless if one field doesn't exist
    ordering = ("sort_order", "-created_at")

    def customer_display(self, obj):
        return getattr(obj, "customer_name", getattr(obj, "name", ""))
    customer_display.short_description = "Customer"