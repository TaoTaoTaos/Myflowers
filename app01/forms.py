from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["model", "picture", "specification", "COLOR", "qty", "unit_price"]
