from django import forms
from .models import FlowerMaterial


class FlowerMaterialForm(forms.ModelForm):
    class Meta:
        model = FlowerMaterial
        fields = "__all__"
