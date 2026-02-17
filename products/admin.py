from django.contrib import admin
from django.utils import timezone
from .models import Category, Product, Bundle, ProductReview
from .forms import ProductForm


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """ Admin model for products """

    form = ProductForm

    list_display = (
        'sku',
        'name', 
        'category', 
        'price', 
        'image'
        )
    
    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    """ Admin model for categories """
    list_display = (
        'friendly_name',
    )

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ("product", "user", "rating", "status", "created_at")
    list_filter = ("status", "rating", "created_at")
    search_fields = ("product__name", "user__username", "title", "body")
    readonly_fields = ("created_at", "updated_at", "approved_at", "approved_by")

    actions = ["approve_reviews", "reject_reviews"]

    def approve_reviews(self, request, queryset):
        queryset = queryset.exclude(status=ProductReview.Status.APPROVED)
        queryset.update(
            status=ProductReview.Status.APPROVED,
            approved_at=timezone.now(),
            approved_by=request.user,
        )
    approve_reviews.short_description = "Approve selected reviews"

    def reject_reviews(self, request, queryset):
        queryset = queryset.exclude(status=ProductReview.Status.REJECTED)
        queryset.update(
            status=ProductReview.Status.REJECTED,
            approved_at=None,
            approved_by=None,
        )
    reject_reviews.short_description = "Reject selected reviews"