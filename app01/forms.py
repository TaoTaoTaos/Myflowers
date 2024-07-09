from django import forms
from .models import FlowerMaterial, Category, Color, Process, Supplier


class FlowerMaterialForm(forms.ModelForm):
    class Meta:
        model = FlowerMaterial
        fields = "__all__"  # 或者手动列出你想要的字段

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["model"].required = True  # 设置为必填字段
        self.fields["image"].required = True  # 设置为必填字段

    def clean(self):
        cleaned_data = super().clean()
        # 在这里可以添加更多的自定义验证逻辑
        return cleaned_data
