from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    expire_date = forms.DateTimeField(input_formats=['%m/%d/%Y %H:%M %p'])

    class Meta:
        model = Product
        fields = [
            "name", "quantity", "company", "expire_date", "price"
        ]
