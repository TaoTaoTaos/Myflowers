# admin.py
from django.contrib import admin
from .models import (
    Grade,
    Category,
    Color,
    Process,
    Supplier,
    CreatedBy,
    FlowerMaterial,
    CustomUser,
)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(CreatedBy)
class CreatedByAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(FlowerMaterial)
class FlowerMaterialAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "model",
        "chinese_name",
        "english_name",
        "scientific_name",
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
        "created_by",
    )
    search_fields = ("chinese_name", "english_name", "scientific_name", "model")
    list_filter = ("category", "grade", "supplier", "process")


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
