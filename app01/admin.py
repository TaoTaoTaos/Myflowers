from django.contrib import admin
from .models import (
    PackagingType,
    Packaging,
    Grade,
    Category,
    Color,
    Process,
    Supplier,
    Comment,
    FlowerMaterial,
    CustomUser,
    ProductType,
    Product,
    ProductMaterial,
    ProductPackaging,
    Quote,
    QuoteItem,
    Customer,
    FollowUpRecord,
    FollowUpAttachment,
    package_name,
)


# 包装类型模型Admin
@admin.register(PackagingType)
class PackagingTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# 包装模型Admin
@admin.register(Packaging)
class PackagingAdmin(admin.ModelAdmin):
    list_display = (
        "model",
        "packaging_type",
        "name",
        "cost_price",
        "selling_price",
        "created_by",
        "created_at",
        "updated_at",
    )
    search_fields = ("model", "name")
    list_filter = ("packaging_type", "created_at", "updated_at")
    readonly_fields = ("model", "created_at", "updated_at")


# 等级模型Admin
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# 分类模型Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# 颜色模型Admin
@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# 处理方式模型Admin
@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# 供应商模型Admin
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# 评论模型Admin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("created_by", "text", "created_at")
    search_fields = ("created_by__username", "text")
    list_filter = ("created_at",)


# 花材模型Admin
@admin.register(FlowerMaterial)
class FlowerMaterialAdmin(admin.ModelAdmin):
    list_display = (
        "model",
        "chinese_name",
        "english_name",
        "cost_price",
        "created_by",
        "created_at",
        "updated_at",
    )
    search_fields = ("model", "chinese_name", "english_name")
    list_filter = ("category", "created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


# 自定义用户模型Admin
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_active", "date_joined")


# 产品类型模型Admin
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# 包装名称模型Admin
@admin.register(package_name)
class PackageNameAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


# 产品模型Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "model",
        "chinese_name",
        "english_name",
        "cost",
        "price",
        "created_by",
        "created_at",
        "updated_at",
    )
    search_fields = ("model", "chinese_name", "english_name")
    list_filter = ("product_type", "created_at", "updated_at")
    readonly_fields = ("cost", "price", "created_at", "updated_at")


# 产品-花材中间模型Admin
@admin.register(ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ("product", "flower_material", "quantity", "ratio")
    search_fields = ("product__chinese_name", "flower_material__chinese_name")


# 产品-包装中间模型Admin
@admin.register(ProductPackaging)
class ProductPackagingAdmin(admin.ModelAdmin):
    list_display = ("product", "packaging", "inner_box_quantity", "outer_box_quantity")
    search_fields = ("product__chinese_name", "packaging__name")


# 报价单模型Admin
@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "buyer",
        "total",
        "grand_total",
        "created_by",
        "created_at",
        "updated_at",
    )
    search_fields = ("buyer",)
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")


# 报价单项模型Admin
@admin.register(QuoteItem)
class QuoteItemAdmin(admin.ModelAdmin):
    list_display = ("quote", "model", "qty", "unit_price", "amount")
    search_fields = ("quote__buyer", "model")


# 客户模型Admin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "customer_id",
        "name",
        "email",
        "status",
        "level",
        "created_by",
        "updated_at",
    )
    search_fields = ("name", "email", "company_name")
    list_filter = ("status", "level", "created_by")
    readonly_fields = ("customer_id", "updated_at")


# 客户跟进记录模型Admin
@admin.register(FollowUpRecord)
class FollowUpRecordAdmin(admin.ModelAdmin):
    list_display = ("customer", "follow_up_count", "follow_up_time", "created_by")
    search_fields = ("customer__name", "created_by__username")
    list_filter = ("follow_up_time", "created_by")


# 跟进附件模型Admin
@admin.register(FollowUpAttachment)
class FollowUpAttachmentAdmin(admin.ModelAdmin):
    list_display = ("follow_up_record", "file")
    search_fields = ("follow_up_record__customer__name",)
