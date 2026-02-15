from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    """
    Form for creating and editing products in the admin/store dashboard
    """

    class Meta:
        model = Product
        fields = (
            "category", 
            "sku",
            "name", 
            "slug",
            "description",
            "product_material",
            "product_dimensions",
            "price", 
            "dice_set_price",
            "image"
        )
        labels = {
            'category': 'Category',
            'sku': 'SKU',
            'name': 'Name',
            'slug': 'Slug',
            'description': 'Description',
            'product_material': 'Material',
            'product_dimensions': 'Dimensions',
            'price': 'Price',
            'dice_set_price': 'Dice Set Price',
            'image': 'Image'
        }

    def __init__(self, *args, **kwargs):
        """
        Add consistent styling to all fields
        """
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-3"
