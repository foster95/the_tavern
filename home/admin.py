from django.contrib import admin
import calendar
from .models import Testimonial, ContactForm, ProductOfTheMonth


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
    list_display = ("customer_display", "quote", "created_at")
    search_fields = ("quote", "customer_name", "name")
    ordering = ("sort_order", "-created_at")

    def customer_display(self, obj):
        return getattr(obj, "customer_name", getattr(obj, "name", ""))
    customer_display.short_description = "Customer"

@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ("topic", "name", "email", "created_at", "is_read", "is_resolved")
    list_filter = ("topic","is_read", "is_resolved", "created_at")
    search_fields = ("name", "email", "message")
    readonly_fields = ("topic", "name", "email", "message", "created_at")
    ordering = ("-created_at",)

    actions = ["mark_read", "mark_resolved"]

    @admin.action(description="Mark selected messages as read")
    def mark_read(self, request, queryset):
        queryset.update(is_read=True)

    @admin.action(description="Mark selected messages as resolved")
    def mark_resolved(self, request, queryset):
        queryset.update(is_resolved=True)