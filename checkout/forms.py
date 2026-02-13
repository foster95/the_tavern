from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "county",
            "postcode",
            "country",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2 (optional)",
            "town_or_city": "Town or City",
            "county": "County (optional)",
            "postcode": "Postcode",
        }

        self.fields["first_name"].widget.attrs["autofocus"] = True

        for field_name, field in self.fields.items():
            # Add your consistent styling class
            existing_classes = field.widget.attrs.get("class", "")
            field.widget.attrs["class"] = f"{existing_classes} stripe-style-input".strip()

            if field_name != "country":
                placeholder = placeholders.get(field_name, field_name.replace("_", " ").title())

                # optional: show * in placeholder if required
                if field.required:
                    placeholder = f"{placeholder} *"

                field.widget.attrs["placeholder"] = placeholder
                field.label = False  # hide label for inputs

        # Country select: keep label hidden if you want, but set an empty_label instead
        self.fields["country"].label = False
        # If you are using django-countries CountryField, this works:
        self.fields["country"].empty_label = "Select Country"
