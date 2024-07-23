from django.contrib import admin
from .models import (
    Grade,
    Category,
    Color,
    Process,
    Supplier,
    FlowerMaterial,
    CustomUser,
    Product,
    ProductMaterial,
)

# Register your models here.


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(FlowerMaterial)
class FlowerMaterialAdmin(admin.ModelAdmin):
    list_display = (
        "model",
        "category",
        "chinese_name",
        "english_name",
        "scientific_name",
        "color",
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
        "created_by",
    )
    search_fields = ("model", "chinese_name", "english_name", "scientific_name")
    list_filter = ("category", "color", "process", "grade", "supplier")


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "model",
        "chinese_name",
        "english_name",
        "labor_cost",
        "loss_rate",
        "created_by",
        "cost",
    )
    search_fields = ("model", "chinese_name", "english_name")
    list_filter = ("created_by",)


@admin.register(ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = (
        "product",
        "flower_material",
        "quantity",
        "ratio",
    )
    search_fields = ("product__chinese_name", "flower_material__chinese_name")
    list_filter = []  # 你可以根据需要添加其他过滤条件
