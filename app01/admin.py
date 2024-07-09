from django.contrib import admin
from .models import Category, Color, Process, Supplier, FlowerMaterial

# Register your models here.


@admin.register(FlowerMaterial)
class FlowerMaterialAdmin(admin.ModelAdmin):
    list_display = (
        "chinese_name",
        "category",
        "color",
        "size",
        "weight",
        "sale_spec",
        "supplier",
        "stock",
    )
    list_filter = ("category", "color", "process", "supplier", "grade")
    search_fields = ("chinese_name", "english_name", "scientific_name")
    list_per_page = 20


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
