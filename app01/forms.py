from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Product, ProductMaterial, FlowerMaterial, QuoteItem

# 包装表单

from django import forms
from .models import Packaging


class PackagingForm(forms.ModelForm):
    class Meta:
        model = Packaging

        fields = [
            "packaging_type",
            "name",
            "length",
            "width",
            "height",
            "cost_price",
            "selling_price",
            "image",
            "remark",
        ]


###################################包装表单###################################
# 用户注册表单
class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "password1", "password2")


# 用户登录表单
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ("username", "password")


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "is_staff",
            "is_superuser",
            "last_login",
            "date_joined",
        ]
        widgets = {
            "username": forms.TextInput(attrs={"readonly": "readonly"}),
            "is_active": forms.CheckboxInput(attrs={"disabled": "disabled"}),
            "is_staff": forms.CheckboxInput(attrs={"disabled": "disabled"}),
            "is_superuser": forms.CheckboxInput(attrs={"disabled": "disabled"}),
            "last_login": forms.TextInput(attrs={"readonly": "readonly"}),
            "date_joined": forms.TextInput(attrs={"readonly": "readonly"}),
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ["old_password", "new_password1", "new_password2"]


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


from django import forms
from .models import Product, ProductMaterial


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "model": forms.TextInput(attrs={"class": "form-control"}),
            "product_type": forms.Select(
                attrs={"class": "form-control"}
            ),  # 新增 product_type 字段
            "chinese_name": forms.TextInput(attrs={"class": "form-control"}),
            "english_name": forms.TextInput(attrs={"class": "form-control"}),
            "size": forms.TextInput(attrs={"class": "form-control"}),
            "weight": forms.TextInput(attrs={"class": "form-control"}),
            "color": forms.TextInput(attrs={"class": "form-control"}),
            "package": forms.TextInput(attrs={"class": "form-control"}),
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
            "profit_margin": forms.NumberInput(attrs={"class": "form-control"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
            "attachment": forms.ClearableFileInput(
                attrs={"class": "form-control-file"}
            ),  # 新增附件字段
        }


class ProductMaterialForm(forms.ModelForm):
    class Meta:
        model = ProductMaterial
        fields = ["flower_material", "quantity", "ratio"]
        widgets = {
            "flower_material": forms.Select(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "ratio": forms.NumberInput(attrs={"class": "form-control"}),
        }


ProductMaterialFormSet = forms.inlineformset_factory(
    Product, ProductMaterial, form=ProductMaterialForm, extra=1, can_delete=True
)

###############报价单################


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
######################客户###############################
from django import forms
from .models import Customer


from django import forms
from .models import Customer


from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            "name",
            "country",
            "company_name",
            "address",
            "phone",
            "mobile",
            "email",
            "sales_channel",
            "product_demand",
            "source",
            "status",
            "level",
            "social_account",
            "website_link",
            "image",
        ]


from .models import FollowUpRecord


# forms.py

from django import forms
from .models import FollowUpRecord, FollowUpAttachment
from .widgets import MultiFileInput


class FollowUpRecordForm(forms.ModelForm):
    class Meta:
        model = FollowUpRecord
        fields = ["details"]
        widgets = {
            "details": forms.Textarea(attrs={"class": "form-control"}),
        }


class FollowUpAttachmentForm(forms.ModelForm):
    class Meta:
        model = FollowUpAttachment
        fields = ["file"]
        widgets = {
            "file": MultiFileInput(attrs={"class": "form-control"}),
        }
