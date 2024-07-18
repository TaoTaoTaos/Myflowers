from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Product, ProductMaterial, FlowerMaterial


# 用户注册表单
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "password1", "password2")


# 用户登录表单
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ("username", "password")


# 花材表单
from django import forms
from .models import FlowerMaterial


class FlowerMaterialForm(forms.ModelForm):
    class Meta:
        model = FlowerMaterial
        fields = [
            "model",
            "category",
            "image",
            "chinese_name",
            "english_name",
            "scientific_name",
            "color",
            "chineses_specifications",
            "size",
            "weight",
            "sale_spec_quantity",
            "sale_spec_unit",
            "process",
            "outer_box_length",
            "outer_box_width",
            "outer_box_height",
            "packing_quantity",
            "grade",
            "supplier",
            "price_one",
            "price_two",
        ]
        widgets = {
            "model": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "chinese_name": forms.TextInput(attrs={"class": "form-control"}),
            "english_name": forms.TextInput(attrs={"class": "form-control"}),
            "scientific_name": forms.TextInput(attrs={"class": "form-control"}),
            "color": forms.TextInput(attrs={"class": "form-control"}),
            "chineses_specifications": forms.TextInput(attrs={"class": "form-control"}),
            "size": forms.TextInput(attrs={"class": "form-control"}),
            "weight": forms.TextInput(attrs={"class": "form-control"}),
            "sale_spec_quantity": forms.TextInput(attrs={"class": "form-control"}),
            "sale_spec_unit": forms.Select(attrs={"class": "form-control"}),
            "process": forms.Select(attrs={"class": "form-control"}),
            "outer_box_length": forms.NumberInput(attrs={"class": "form-control"}),
            "outer_box_width": forms.NumberInput(attrs={"class": "form-control"}),
            "outer_box_height": forms.NumberInput(attrs={"class": "form-control"}),
            "packing_quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "grade": forms.Select(attrs={"class": "form-control"}),
            "supplier": forms.Select(attrs={"class": "form-control"}),
            "price_one": forms.NumberInput(attrs={"class": "form-control"}),
            "price_two": forms.NumberInput(attrs={"class": "form-control"}),
        }


# 产品表单
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "model",
            "chinese_name",
            "english_name",
            "labor_cost",
            "loss_rate",
            "description",
        ]
        exclude = ("created_by",)  # 排除created_by字段

    flower_materials = forms.ModelMultipleChoiceField(
        queryset=FlowerMaterial.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="选择花材",
    )


# 产品材料表单
class ProductMaterialForm(forms.ModelForm):
    class Meta:
        model = ProductMaterial
        fields = ["flower_material", "quantity", "ratio", "price_type"]
