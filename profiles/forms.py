from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ("user", "profile_picture")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "default_first_name": "First Name",
            "default_last_name": "Last Name",
            "default_phone_number": "Phone Number",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_town_or_city": "Town or City",
            "default_county": "County / State",
            "default_postcode": "Postal Code",
        }

        if "default_first_name" in self.fields:
            self.fields["default_first_name"].widget.attrs["autofocus"] = True

        for field_name, field in self.fields.items():
            if field_name != "default_country":
                field.label = False

            field.widget.attrs["class"] = "stripe-style-input"

            if field_name != "default_country":
                placeholder = placeholders.get(
                    field_name,
                    field_name.replace("_", " ").title()
                )
                if field.required:
                    placeholder = f"{placeholder} *"
                field.widget.attrs["placeholder"] = placeholder
