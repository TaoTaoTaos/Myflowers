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
    ShippingMethod,
    Order,
    OrderItem,
    OrderProfit,
)

############################### 包装相关模型 ###############################


@admin.register(PackagingType)
class PackagingTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    # 包装类型模型管理界面


@admin.register(Packaging)
class PackagingAdmin(admin.ModelAdmin):
    list_display = [
        "model",
        "packaging_type",
        "name",
        "cost_price",
        "selling_price",
        "created_by",
        "created_at",
        "updated_at",
    ]
    search_fields = ["model", "name"]
    list_filter = ["packaging_type", "created_by"]
    readonly_fields = ["model"]
    # 包装模型管理界面


############################### 花材相关模型 ###############################


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    # 等级模型管理界面


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    # 分类模型管理界面


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    # 颜色模型管理界面


@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    # 处理方式模型管理界面


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    # 供应商模型管理界面


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["created_by", "created_at"]
    search_fields = ["created_by__username", "text"]
    list_filter = ["created_by", "created_at"]
    # 评论模型管理界面


@admin.register(FlowerMaterial)
class FlowerMaterialAdmin(admin.ModelAdmin):
    list_display = [
        "model",
        "chinese_name",
        "category",
        "color",
        "grade",
        "supplier",
        "cost_price",
        "price_one",
        "price_two",
        "created_by",
        "created_at",
        "updated_at",
    ]
    search_fields = ["model", "chinese_name", "english_name"]
    list_filter = ["category", "color", "grade", "supplier", "created_by"]
    readonly_fields = ["model"]
    # 花材模型管理界面


############################### 用户模型 ###############################


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "is_staff", "is_active"]
    search_fields = ["username", "email"]
    list_filter = ["is_staff", "is_active"]
    # 用户模型管理界面


############################### 产品相关模型 ###############################


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    # 产品类型模型管理界面


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "model",
        "chinese_name",
        "product_type",
        "color",
        "labor_cost",
        "loss_rate",
        "profit_margin",
        "created_by",
        "created_at",
        "updated_at",
    ]
    search_fields = ["model", "chinese_name", "english_name"]
    list_filter = ["product_type", "color", "created_by"]
    readonly_fields = ["model"]
    # 产品模型管理界面


@admin.register(ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ["product", "flower_material", "quantity", "ratio"]
    search_fields = ["product__model", "flower_material__model"]
    list_filter = ["product", "flower_material"]
    # 产品-花材中间模型管理界面


@admin.register(ProductPackaging)
class ProductPackagingAdmin(admin.ModelAdmin):
    list_display = ["product", "packaging", "inner_box_quantity", "outer_box_quantity"]
    search_fields = ["product__model", "packaging__model"]
    list_filter = ["product", "packaging"]
    # 产品-包装中间模型管理界面


############################### 报价单相关模型 ###############################


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "buyer",
        "date",
        "total",
        "grand_total",
        "created_by",
        "created_at",
        "updated_at",
    ]
    search_fields = ["buyer", "id"]
    list_filter = ["created_by", "date", "created_at"]
    # 报价单模型管理界面


@admin.register(QuoteItem)
class QuoteItemAdmin(admin.ModelAdmin):
    list_display = ["quote", "model", "qty", "unit_price", "amount"]
    search_fields = ["quote__id", "model"]
    list_filter = ["quote"]
    # 报价单项模型管理界面


############################### 客户相关模型 ###############################


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = [
        "customer_id",
        "name",
        "country",
        "company_name",
        "email",
        "status",
        "level",
        "created_by",
        "updated_at",
    ]
    search_fields = ["customer_id", "name", "company_name", "email"]
    list_filter = ["country", "status", "level", "created_by"]
    # 客户模型管理界面


@admin.register(FollowUpRecord)
class FollowUpRecordAdmin(admin.ModelAdmin):
    list_display = ["customer", "follow_up_count", "follow_up_time", "created_by"]
    search_fields = ["customer__name", "created_by__username"]
    list_filter = ["follow_up_time", "created_by"]
    # 跟进记录模型管理界面


@admin.register(FollowUpAttachment)
class FollowUpAttachmentAdmin(admin.ModelAdmin):
    list_display = ["follow_up_record", "file"]
    search_fields = ["follow_up_record__customer__name"]
    list_filter = ["follow_up_record"]
    # 跟进附件模型管理界面


############################### 发货方式模型 ###############################


@admin.register(ShippingMethod)
class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    # 发货方式模型管理界面


############################### 订单相关模型 ###############################


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        "order_number",
        "customer",
        "order_date",
        "shipment_date",
        "actual_shipment_date",
        "status",
        "preparation_status",
        "created_by",
        "created_at",
        "updated_at",
    ]
    search_fields = ["order_number", "customer__name"]
    list_filter = ["status", "preparation_status", "order_date", "created_by"]
    # 订单模型管理界面


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        "order",
        "product",
        "flower_material",
        "quantity",
        "unit_price",
        "total_price",
    ]
    search_fields = ["order__order_number", "product__model", "flower_material__model"]
    list_filter = ["order", "product", "flower_material"]
    # 订单项模型管理界面


@admin.register(OrderProfit)
class OrderProfitAdmin(admin.ModelAdmin):
    list_display = ["order", "theoretical_profit", "actual_profit"]
    search_fields = ["order__order_number"]
    list_filter = ["order"]
    # 订单利润模型管理界面
