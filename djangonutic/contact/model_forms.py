from django import forms
from .models import Contact


class CreateContact(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "body"]
