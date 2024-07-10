from django import forms
from django.db import models
from .models import FlowerMaterial

from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("username", "password1", "password2")


# 确认登录
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
        self.fields["model"].label = "模型"
        self.fields["image"].label = "图片"
        self.fields["chinese_name"].label = "中文名"
        self.fields["english_name"].label = "英文名"
        self.fields["scientific_name"].label = "学名"
        self.fields["color"].label = "颜色"
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
        self.fields["stock"].label = "库存数量"

        # 设置必填字段
        self.fields["model"].required = True
        self.fields["image"].required = True

    def clean(self):
        cleaned_data = super().clean()
        required_fields = ["model", "image"]  # 添加所有必填字段的名称

        for field_name in required_fields:
            if not cleaned_data.get(field_name):
                self.add_error(field_name, "该字段不能为空")
        return cleaned_data
