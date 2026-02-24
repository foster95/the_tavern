from django import forms
from .models import ContactForm

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ["topic", "name", "email", "message"]
        widgets = {
            "topic": forms.Select(attrs={"class": "form-control"}),
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "message": forms.Textarea(attrs={"class": "form-control", "rows": 6}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["topic"].choices = [
            ("", "How can the Guild assist you?")
        ] + list(self.fields["topic"].choices)

        self.fields["topic"].required = True