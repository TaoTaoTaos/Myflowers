from django.contrib import admin
from .models import Category, Color, Process, Supplier, FlowerMaterial, CustomUser
from django.contrib.auth.admin import UserAdmin


# 注册Category模型
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# 注册Color模型
class ColorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# 注册Process模型
class ProcessAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# 注册Supplier模型
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# 注册FlowerMaterial模型
class FlowerMaterialAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "model",
        "chinese_name",
        "english_name",
        "scientific_name",
        "color",
        "size",
        "weight",
        "sale_spec",
        "process",
        "outer_box_size",
        "packing_quantity",
        "grade",
        "supplier",
        "price_one",
        "price_two",
        "stock",
    )
    search_fields = ("model", "chinese_name", "english_name", "scientific_name")
    list_filter = ("category", "color", "process", "supplier", "grade")


# 注册CustomUser模型
class CustomUserAdmin(UserAdmin):
    model = CustomUser


admin.site.register(Category, CategoryAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Process, ProcessAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(FlowerMaterial, FlowerMaterialAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
