from django import forms
from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser, Product, ProductMaterial, FlowerMaterial


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "password1", "password2")


# 确认登录
class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ("username", "password")


from django import forms
from django.db import models
from .models import FlowerMaterial, CustomUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "password1", "password2")


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ("username", "password")


class FlowerMaterialForm(forms.ModelForm):
    class Meta:
        model = FlowerMaterial
        fields = "__all__"  # 或者手动列出你想要的字段

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 设置中文标签
        self.fields["category"].label = "类别"
        self.fields["model"].label = "型号"
        self.fields["image"].label = "图片"
        self.fields["chinese_name"].label = "中文名"
        self.fields["english_name"].label = "英文名"
        self.fields["scientific_name"].label = "学名"
        self.fields["size"].label = "尺寸（cm）"
        self.fields["weight"].label = "重量（g）"
        self.fields["sale_spec_quantity"].label = "销售规格数量"
        self.fields["sale_spec_unit"].label = "销售规格单位"
        self.fields["process"].label = "加工方式"
        self.fields["outer_box_length"].label = "外箱长度（cm）"
        self.fields["outer_box_width"].label = "外箱宽度（cm）"
        self.fields["outer_box_height"].label = "外箱高度（cm）"
        self.fields["packing_quantity"].label = "装箱数量"
        self.fields["grade"].label = "等级"
        self.fields["supplier"].label = "供应商"
        self.fields["price_one"].label = "价格一"
        self.fields["price_two"].label = "价格二"
        self.fields["created_by"].label = "创建者"

        # 设置默认值
        self.fields["chinese_name"].initial = "默认名"
        self.fields["english_name"].initial = "Default Name"
        self.fields["scientific_name"].initial = "Default Scientific Name"
        self.fields["size"].initial = 0.0
        self.fields["weight"].initial = 0.0
        self.fields["sale_spec_quantity"].initial = 1
        self.fields["outer_box_length"].initial = 0.0
        self.fields["outer_box_width"].initial = 0.0
        self.fields["outer_box_height"].initial = 0.0
        self.fields["packing_quantity"].initial = 1

        self.fields["price_one"].initial = 0.0
        self.fields["price_two"].initial = 0.0
        # 设置必填字段
        self.fields["model"].required = True
        self.fields["category"].required = True
        self.fields["created_by"].required = True

    def clean(self):
        cleaned_data = super().clean()
        required_fields = ["model", "category", "created_by"]  # 添加所有必填字段的名称

        for field in required_fields:
            if not cleaned_data.get(field):
                self.add_error(field, "有必填项未填。")

        return cleaned_data


###########################################


from django import forms
from .models import Product, ProductMaterial


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "description",
            "model",
            "chinese_name",
            "english_name",
            "labor_cost",
            "loss_rate",
            "created_by",
        ]


class ProductMaterialForm(forms.ModelForm):
    class Meta:
        model = ProductMaterial
        fields = ["flower_material", "quantity", "ratio", "price_type"]
