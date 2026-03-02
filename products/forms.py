from django import forms
from .models import Product, ProductReview


class ProductForm(forms.ModelForm):
    """
    Form for creating and editing products
    """

    is_dice_set = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={"class": "form-check-input"}),
        label="Is this a dice set?"
    )

    class Meta:
        model = Product
        fields = (
            "category",
            "name",
            "description",
            "product_material",
            "product_dimensions",
            "is_dice_set",
            "price",
            "dice_set_price",
            "image",
        )

        labels = {
            "price": "Flat Price (for single dice or non-dice products)",
            "dice_set_price": "Full Set Price",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():

            if field_name == "is_dice_set":
                field.widget.attrs["class"] = "form-check-input"
                continue

            if field.widget.__class__.__name__ in ("Select", "SelectMultiple"):
                field.widget.attrs["class"] = "form-select rounded-3"
            else:
                field.widget.attrs["class"] = "form-control rounded-3"
        self.fields["category"].label_from_instance = (
            lambda obj: obj.friendly_name or obj.name
        )

    def clean(self):
        cleaned = super().clean()
        is_dice_set = cleaned.get("is_dice_set")
        price = cleaned.get("price")
        dice_set_price = cleaned.get("dice_set_price")

        if price is None:
            self.add_error("price", "Please enter a price for this product.")

        if is_dice_set:
            if dice_set_price is None:
                self.add_error(
                    "dice_set_price", "Please add a full set price."
                    )
        else:
            cleaned["dice_set_price"] = None

        return cleaned


class ProductReviewForm(forms.ModelForm):
    rating = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = ProductReview
        fields = ["rating", "title", "body"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
        }
