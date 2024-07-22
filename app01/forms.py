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


##################################################
from django.forms import inlineformset_factory
from .models import Product, ProductMaterial, FlowerMaterial


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "model": forms.TextInput(attrs={"class": "form-control"}),
            "chinese_name": forms.TextInput(attrs={"class": "form-control"}),
            "english_name": forms.TextInput(attrs={"class": "form-control"}),
            "size": forms.TextInput(attrs={"class": "form-control"}),
            "weight": forms.TextInput(attrs={"class": "form-control"}),
            "color": forms.TextInput(attrs={"class": "form-control"}),
            "Package": forms.TextInput(attrs={"class": "form-control"}),
            "sale_spec_quantity": forms.TextInput(attrs={"class": "form-control"}),
            "sale_spec_unit": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "inner_box_long": forms.NumberInput(attrs={"class": "form-control"}),
            "inner_box_width": forms.NumberInput(attrs={"class": "form-control"}),
            "inner_box_height": forms.NumberInput(attrs={"class": "form-control"}),
            "outer_box_length": forms.NumberInput(attrs={"class": "form-control"}),
            "outer_box_width": forms.NumberInput(attrs={"class": "form-control"}),
            "outer_box_height": forms.NumberInput(attrs={"class": "form-control"}),
            "labor_cost": forms.NumberInput(attrs={"class": "form-control"}),
            "loss_rate": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        }


class ProductMaterialForm(forms.ModelForm):
    class Meta:
        model = ProductMaterial
        fields = ["flower_material", "quantity", "ratio", "price_type"]


ProductMaterialFormSet = forms.inlineformset_factory(
    Product, ProductMaterial, form=ProductMaterialForm, extra=1, can_delete=True
)

###############报价单################
from django import forms
from .models import QuoteItem


class QuoteItemForm(forms.ModelForm):
    class Meta:
        model = QuoteItem
        fields = [
            "model",
            "picture",
            "specification",
            "color",
            "qty",
            "cost_price",
            "profit_margin",
        ]
        widgets = {
            "model": forms.TextInput(attrs={"class": "form-control"}),
            "picture": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "specification": forms.TextInput(attrs={"class": "form-control"}),
            "color": forms.TextInput(attrs={"class": "form-control"}),
            "qty": forms.NumberInput(attrs={"class": "form-control"}),
            "cost_price": forms.NumberInput(attrs={"class": "form-control"}),
            "profit_margin": forms.NumberInput(attrs={"class": "form-control"}),
        }


###############报价单end################
