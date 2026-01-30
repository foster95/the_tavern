from django.contrib import admin
import calendar
from .models import ProductOfTheMonth

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
