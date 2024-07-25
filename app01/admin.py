from django.contrib import admin
from .models import (
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
    Quote,
    QuoteItem,
    Customer,
    FollowUpRecord,
    FollowUpAttachment,
)


# 注册花材相关模型
@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(FlowerMaterial)
class FlowerMaterialAdmin(admin.ModelAdmin):
    list_display = (
        "model",
        "chinese_name",
        "english_name",
        "category",
        "color",
        "cost_price",
    )
    search_fields = ("model", "chinese_name", "english_name")


# 注册用户模型
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_active")
    search_fields = ("username", "email")


# 注册产品类型模型
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


# 注册产品模型
class ProductMaterialInline(admin.TabularInline):
    model = ProductMaterial
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("model", "chinese_name", "english_name", "product_type", "price")
    search_fields = ("model", "chinese_name", "english_name")
    inlines = [ProductMaterialInline]


# 注册报价单模型
class QuoteItemInline(admin.TabularInline):
    model = QuoteItem
    extra = 1


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("id", "buyer", "date", "grand_total")
    search_fields = ("buyer",)
    inlines = [QuoteItemInline]


@admin.register(QuoteItem)
class QuoteItemAdmin(admin.ModelAdmin):
    list_display = ("quote", "model", "qty", "unit_price", "amount")
    search_fields = ("quote__buyer", "model")


# 注册客户模型
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("customer_id", "name", "company_name", "email", "status")
    search_fields = ("name", "company_name", "email")


# 注册客户跟进记录模型
class FollowUpAttachmentInline(admin.TabularInline):
    model = FollowUpAttachment
    extra = 1


@admin.register(FollowUpRecord)
class FollowUpRecordAdmin(admin.ModelAdmin):
    list_display = ("customer", "follow_up_count", "follow_up_time", "created_by")
    search_fields = ("customer__name",)
    inlines = [FollowUpAttachmentInline]


# 注册评论模型
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("created_by", "text", "created_at")
    search_fields = ("created_by__username", "text")
