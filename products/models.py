from django.db import models
import uuid
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    """ Model for product categories """

    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.friendly_name or self.name
    
    def get_friendly_name(self):
        return self.friendly_name

def generate_sku(product):
    category_code = product.category.slug[:3].upper() if product.category else "GEN"
    material = (product.product_material or "STD")[:8].replace(" ", "").upper()
    name_part = slugify(product.name).split("-")[-1][:6].upper()
    unique = uuid.uuid4().hex[:4].upper()
    return f"{category_code}-{material}-{name_part}-{unique}"
        

class Product(models.Model):
    """ Model for products """

    class Meta:
        ordering = ['name']
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL, related_name='products'
    )
    sku = models.CharField(max_length=50, null=True, blank=True, unique=True)
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True, null=True, blank=True)
    description = models.TextField()
    product_material = models.CharField(max_length=254, null=True, blank=True)
    product_dimensions = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    dice_set_price= models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null= True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            
        if not self.sku:
            self.sku = generate_sku(self)
                
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Bundle(models.Model):
    """ Model for product bundles - ie is customer buying one d20 or a full set? """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='bundle_prices'
    )
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        unique_together = ('category', 'name')

    def __str__(self):
        return f"{self.category.name} - {self.name}"
    