from django.contrib import admin
from .models import FlowerMaterial, Category, Color, Process, Supplier, Created_by

# Register your models here.
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Process)
admin.site.register(Supplier)
admin.site.register(Created_by)


@admin.register(FlowerMaterial)
class FlowerMaterialAdmin(admin.ModelAdmin):
    list_display = ("model", "category", "created_by")  # 在列表中显示的字段
    list_filter = ("category", "created_by")  # 过滤器
    search_fields = ("model", "chinese_name", "english_name")  # 搜索字段
    ordering = ("model",)  # 排序方式

    # 定义字段集
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "category",
                    "model",
                    "image",
                    "chinese_name",
                    "english_name",
                    "scientific_name",
                )
            },
        ),
        (
            "尺寸和重量",
            {
                "fields": ("size", "weight"),
            },
        ),
        (
            "销售规格",
            {
                "fields": ("sale_spec_quantity", "sale_spec_unit"),
            },
        ),
        (
            "工艺",
            {
                "fields": ("process",),
            },
        ),
        (
            "外箱尺寸",
            {
                "fields": (
                    "outer_box_length",
                    "outer_box_width",
                    "outer_box_height",
                    "outer_box_size",
                ),
            },
        ),
        (
            "包装",
            {
                "fields": ("packing_quantity", "grade"),
            },
        ),
        (
            "供应商和价格",
            {
                "fields": ("supplier", "price_one", "price_two"),
            },
        ),
        (
            "创建者",
            {
                "fields": ("created_by",),
            },
        ),
    )

    # 处理空白字段的显示问题
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "created_by":
            kwargs["queryset"] = Created_by.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
