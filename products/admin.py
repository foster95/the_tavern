from django.contrib import admin
from .models import Category, Product, Bundle

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    """ Admin model for products """
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