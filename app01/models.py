from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from decimal import Decimal
from django.conf import settings

###############################包装相关模型###################################
from django.db import models
from django.utils import timezone
from django.conf import settings
import os
import re


# 包装类型模型
class PackagingType(models.Model):
    TYPE_CHOICES = [
        ("内盒", "Inner Box"),
        ("外箱", "Outer Box"),
        ("花器", "Flower Vessel"),
    ]

    name = models.CharField(max_length=100, choices=TYPE_CHOICES, unique=True)

    def __str__(self):
        return self.name


# 自定义文件上传路径函数
def packaging_directory_path(instance, filename):
    # Replace any non-alphanumeric character with an underscore
    safe_model_name = re.sub(r"[^\w\s-]", "", instance.model)
    safe_model_name = re.sub(r"[-\s]+", "-", safe_model_name).strip("-_")
    # file will be uploaded to MEDIA_ROOT/packaging_images/Packaging/<model_name>/<filename>
    return os.path.join("packaging_images", "Packaging", safe_model_name, filename)


# 包装模型
class Packaging(models.Model):
    model = models.CharField(max_length=100, primary_key=True, editable=False)
    packaging_type = models.ForeignKey(
        PackagingType, on_delete=models.SET_NULL, null=True
    )
    image = models.ImageField(upload_to=packaging_directory_path, null=True, blank=True)
    name = models.CharField(max_length=200)
    length = models.FloatField(help_text="长度，单位：cm", null=True, blank=True)
    width = models.FloatField(help_text="宽度，单位：cm", null=True, blank=True)
    height = models.FloatField(help_text="高度，单位：cm", null=True, blank=True)
    cost_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0.0
    )
    selling_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0.0
    )
    remark = models.CharField(max_length=200, blank=True, default="无备注")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        if not self.model:
            existing_packagings = Packaging.objects.filter(
                packaging_type=self.packaging_type
            ).count()
            self.model = f"{self.packaging_type.name}-{existing_packagings + 1:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


###############################包装相关模型end###################################
#
##############################花材相关模型#####################################


# 等级模型
class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 分类模型
class Category(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


# 颜色模型
class Color(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


# 处理方式模型
class Process(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


# 供应商模型
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


from django.db import models
from django.contrib.auth.models import User


# 评论模型
class Comment(models.Model):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


from datetime import datetime


# 花材模型
class FlowerMaterial(models.Model):
    model = models.CharField(
        max_length=100, blank=False, default="Material0000", primary_key=True
    )
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, default="默认类型"
    )
    image = models.ImageField(upload_to="images/", null=True, blank=True, default=None)
    chinese_name = models.CharField(max_length=200, null=True, blank=True, default="")
    english_name = models.CharField(max_length=200, null=True, blank=True, default="")
    scientific_name = models.CharField(
        max_length=200, null=True, blank=True, default=""
    )
    color = models.CharField(max_length=200, null=True, blank=True, default="")
    chineses_specifications = models.CharField(
        max_length=200, null=True, blank=True, default="无中文规格"
    )
    size = models.CharField(
        max_length=200, help_text="单位：cm", blank=True, default=""
    )
    weight = models.CharField(
        max_length=200, help_text="单位：g", blank=True, default=""
    )
    sale_spec_quantity = models.CharField(
        max_length=200, help_text="销售规格的数字", blank=True, default=""
    )
    sale_spec_unit = models.CharField(
        max_length=10,
        help_text="销售规格的单位",
        choices=[("pcs", "pcs"), ("g", "g"), ("box", "box"), ("kg", "kg")],
        blank=True,
        null=True,
        default="pcs",
    )
    process = models.ForeignKey(
        Process, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    outer_box_length = models.FloatField(
        help_text="长度，单位：cm", null=True, blank=True, default=0.0
    )
    outer_box_width = models.FloatField(
        help_text="宽度，单位：cm", null=True, blank=True, default=0.0
    )
    outer_box_height = models.FloatField(
        help_text="高度，单位：cm", null=True, blank=True, default=0.0
    )
    packing_quantity = models.IntegerField(
        help_text="单位：qty", null=True, blank=True, default=0
    )
    grade = models.ForeignKey(
        Grade, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    supplier = models.ForeignKey(
        Supplier, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )
    cost_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0.0
    )  # 成本价
    price_one = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0.0
    )
    price_two = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0.0
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.chinese_name if self.chinese_name else self.model

    @property
    def outer_box_size(self):
        return (
            f"{self.outer_box_length} * {self.outer_box_width} * {self.outer_box_height} cm"
            if self.outer_box_length and self.outer_box_width and self.outer_box_height
            else ""
        )

    @property
    def sale_spec(self):
        return (
            f"{self.sale_spec_quantity} {self.sale_spec_unit}"
            if self.sale_spec_quantity and self.sale_spec_unit
            else ""
        )


# 自定义用户模型
class CustomUser(AbstractUser):
    def __str__(self):
        return self.username


##############################产品#####################################
from django.db import models
from django.utils import timezone
from django.conf import settings
from decimal import Decimal
import os
import re


# 自定义文件上传路径函数
def packaging_directory_path(instance, filename):
    # Replace any non-alphanumeric character with an underscore
    safe_model_name = re.sub(r"[^\w\s-]", "", instance.model)
    safe_model_name = re.sub(r"[-\s]+", "-", safe_model_name).strip("-_")
    # file will be uploaded to MEDIA_ROOT/packaging_images/Packaging/<model_name>/<filename>
    return os.path.join("packaging_images", "Packaging", safe_model_name, filename)


# 包装模型
class Packaging(models.Model):
    model = models.CharField(max_length=100, primary_key=True, editable=False)
    packaging_type = models.ForeignKey(
        PackagingType, on_delete=models.SET_NULL, null=True
    )
    image = models.ImageField(upload_to=packaging_directory_path, null=True, blank=True)
    name = models.CharField(max_length=200)
    length = models.FloatField(help_text="长度，单位：cm", null=True, blank=True)
    width = models.FloatField(help_text="宽度，单位：cm", null=True, blank=True)
    height = models.FloatField(help_text="高度，单位：cm", null=True, blank=True)
    cost_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0.0
    )
    selling_price = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0.0
    )
    remark = models.CharField(blank=True, max_length=200, default="无备注")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        if not self.model:
            existing_packagings = Packaging.objects.filter(
                packaging_type=self.packaging_type
            ).count()
            self.model = f"{self.packaging_type.name}-{existing_packagings + 1:04d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


# 产品类型模型
class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 自定义文件上传路径函数
def product_directory_path(instance, filename):
    # Replace any non-alphanumeric character with an underscore
    safe_model_name = re.sub(r"[^\w\s-]", "", instance.model)
    safe_model_name = re.sub(r"[-\s]+", "-", safe_model_name).strip("-_")
    # file will be uploaded to MEDIA_ROOT/products/<model_name>/<filename>
    return os.path.join("products", safe_model_name, filename)


class package_name(models.Model):
    TYPE_CHOICES = [
        ("OOP Bag", "OOP Bag"),
    ]

    name = models.CharField(max_length=100, choices=TYPE_CHOICES, unique=True)

    def __str__(self):
        return self.name


# 产品模型
class Product(models.Model):
    model = models.CharField(
        max_length=100, blank=False, default="Product0000", primary_key=True
    )
    product_type = models.ForeignKey(
        ProductType, on_delete=models.SET_NULL, null=True, blank=True
    )
    package_name = models.ForeignKey(
        package_name, on_delete=models.SET_NULL, null=True, blank=True
    )
    image = models.ImageField(
        upload_to=product_directory_path, null=True, blank=True, default=None
    )
    attachment = models.FileField(
        upload_to=product_directory_path, null=True, blank=True
    )  # 支持上传视频
    materials = models.ManyToManyField("FlowerMaterial", through="ProductMaterial")
    chinese_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200)
    size = models.CharField(max_length=200, blank=True, default="0")
    weight = models.CharField(max_length=200, blank=True, default="0")
    color = models.CharField(max_length=200, blank=True, default="默认颜色")
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    loss_rate = models.FloatField(default=0.0)
    profit_margin = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    description = models.CharField(max_length=200, blank=True, default="无描述")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
    )
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    @property
    def inner_box_size(self):
        inner_box = self.productpackaging_set.filter(
            packaging__packaging_type__name="内盒"
        ).first()
        return (
            f"{inner_box.packaging.length} * {inner_box.packaging.width} * {inner_box.packaging.height} cm"
            if inner_box
            else ""
        )

    @property
    def outer_box_size(self):
        outer_box = self.productpackaging_set.filter(
            packaging__packaging_type__name="外箱"
        ).first()
        return (
            f"{outer_box.packaging.length} * {outer_box.packaging.width} * {outer_box.packaging.height} cm"
            if outer_box
            else ""
        )

    @property
    def cost(self):
        total_cost = Decimal(0)
        for material in self.productmaterial_set.all():
            material_cost = (
                material.flower_material.cost_price
                * Decimal(material.quantity)
                * Decimal(material.ratio)
            )
            total_cost += material_cost
        total_cost += self.labor_cost
        total_cost *= Decimal(1 + self.loss_rate)
        return total_cost

    @property
    def price(self):
        return self.cost * Decimal(1 + self.profit_margin / 100)

    def __str__(self):
        return self.chinese_name


# 产品-花材中间模型
class ProductMaterial(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    flower_material = models.ForeignKey(FlowerMaterial, on_delete=models.CASCADE)
    quantity = models.FloatField(default=1.0)
    ratio = models.FloatField(default=1.0)

    def __str__(self):
        return f"{self.product.chinese_name} - {self.flower_material.chinese_name} x {self.quantity} (Ratio: {self.ratio})"


# 产品-包装中间模型
class ProductPackaging(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    packaging = models.ForeignKey(Packaging, on_delete=models.CASCADE)
    inner_box_quantity = models.PositiveIntegerField(
        default=0, help_text="一个内箱能装多少个产品", null=True, blank=True
    )
    outer_box_quantity = models.PositiveIntegerField(
        default=0, help_text="一个大外箱能装多少内箱", null=True, blank=True
    )

    def __str__(self):
        return f"{self.product.chinese_name} - {self.packaging.name}"


####################################报价单##########################################

from django.db import models
from django.utils import timezone
from django.conf import settings


# 报价单模型
class Quote(models.Model):
    id = models.AutoField(primary_key=True)  # 自增的报价单单号
    shipper = models.CharField(max_length=255, default="Summer Flora.Co.,Ltd.")
    buyer = models.CharField(max_length=255)
    receiver = models.CharField(max_length=255)
    tel = models.CharField(max_length=20)
    invoice_no = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    valid_date = models.DateField()
    freight_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    payment_term = models.CharField(max_length=100, default=" ")
    deliver_time = models.CharField(max_length=100, default=" ")
    payment_currency = models.CharField(max_length=10, default="USD")
    beneficiary_account_number = models.CharField(max_length=50, default=" ")
    swift_code = models.CharField(max_length=11, default=" ")
    beneficiary_country = models.CharField(max_length=50, default=" ")
    beneficiary_name = models.CharField(
        max_length=100, default="Yunnan Summer Flora Co., Ltd."
    )
    beneficiary_address = models.CharField(max_length=255, default=" ")
    beneficiary_bank = models.CharField(
        max_length=100,
        default="",
    )
    beneficiary_bank_address = models.CharField(
        max_length=255,
        default=" ",
    )
    bank_code = models.CharField(max_length=10, default=" ")
    branch_code = models.CharField(max_length=10, default=" ")
    remark = models.TextField(blank=True, default=" ")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
    )
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Quote #{self.id} - {self.buyer}"


from django.db import models
from decimal import Decimal


# 报价单项模型
class QuoteItem(models.Model):
    quote = models.ForeignKey(Quote, related_name="items", on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="quote_items/", null=True, blank=True)
    specification = models.CharField(max_length=200)
    color = models.CharField(max_length=100)
    qty = models.PositiveIntegerField(default=1)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)  # 成本价
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # 客单价
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    profit_margin = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.0
    )  # 利润率

    def save(self, *args, **kwargs):
        # 计算客户单价
        self.unit_price = (
            self.cost_price * Decimal(1 + self.profit_margin / 100)
        ).quantize(Decimal("0.01"))
        self.amount = self.unit_price * Decimal(self.qty)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.model} - {self.qty} x {self.unit_price}"


##################################报价单end#############################

###################################客户#######################################

from django.db import models
from django.contrib.auth import get_user_model
import re
import os

User = get_user_model()


# 客户模型
class Customer(models.Model):
    CUSTOMER_STATUS_CHOICES = [
        ("跟进中", "跟进中"),
        ("已付款", "已付款"),
        ("已成交", "已成交"),
        ("已放弃", "已放弃"),
    ]
    CUSTOMER_LEVEL_CHOICES = [
        ("A", "A"),
        ("B", "B"),
        ("C", "C"),
        ("D", "D"),
    ]

    customer_id = models.CharField(max_length=100, unique=True, editable=False)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True)
    sales_channel = models.CharField(max_length=100, blank=True, null=True)
    product_demand = models.CharField(max_length=255, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=10, choices=CUSTOMER_STATUS_CHOICES, default="跟进中"
    )
    level = models.CharField(max_length=1, choices=CUSTOMER_LEVEL_CHOICES, default="A")
    social_account = models.CharField(max_length=255, blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="customer_images/", blank=True, null=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customers"
    )
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.customer_id:
            username = self.created_by.username
            existing_customers = Customer.objects.filter(
                created_by=self.created_by
            ).count()
            self.customer_id = f"{username}-{existing_customers + 1:04d}"
        super().save(*args, **kwargs)


# 客户跟进记录模型
class FollowUpRecord(models.Model):
    customer = models.ForeignKey(
        Customer, related_name="follow_ups", on_delete=models.CASCADE
    )
    follow_up_count = models.PositiveIntegerField()
    follow_up_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()


# 文件上传路径函数
def user_directory_path(instance, filename):
    # Replace any non-alphanumeric character with an underscore
    safe_customer_name = re.sub(
        r"[^\w\s-]", "", instance.follow_up_record.customer.name
    )
    safe_customer_name = re.sub(r"[-\s]+", "-", safe_customer_name).strip("-_")
    # file will be uploaded to MEDIA_ROOT/<username>/<customer_name>/<filename>
    return os.path.join(
        instance.follow_up_record.created_by.username, safe_customer_name, filename
    )


# 跟进附件模型
class FollowUpAttachment(models.Model):
    follow_up_record = models.ForeignKey(
        FollowUpRecord, related_name="attachments", on_delete=models.CASCADE
    )
    file = models.FileField(upload_to=user_directory_path)


###################################客户end#######################################


from django.db import models
from django.utils import timezone
from django.conf import settings
from decimal import Decimal

############# 发货方式模型 #############


class ShippingMethod(models.Model):
    # 发货方式模型
    name = models.CharField(max_length=100, unique=True, verbose_name="发货方式")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "发货方式"
        verbose_name_plural = "发货方式"


############# 订单模型 #############


class Order(models.Model):
    # 订单状态选择
    ORDER_STATUS_CHOICES = [
        ("pending", "待处理"),
        ("confirmed", "已确认"),
        ("shipped", "已发货"),
        ("delivered", "已送达"),
        ("canceled", "已取消"),
    ]
    # 备货状态选择
    PREPARATION_STATUS_CHOICES = [
        ("not_started", "未开始"),
        ("in_progress", "进行中"),
        ("completed", "已完成"),
    ]

    order_number = models.CharField(
        max_length=100, unique=True, verbose_name="订单号"
    )  # 订单号
    customer = models.ForeignKey(
        "Customer", on_delete=models.SET_NULL, null=True, verbose_name="客户"
    )  # 客户
    order_date = models.DateTimeField(
        default=timezone.now, verbose_name="订单日期"
    )  # 订单日期
    shipment_date = models.DateField(
        verbose_name="应发货日期", null=True, blank=True
    )  # 应发货日期
    actual_shipment_date = models.DateField(
        verbose_name="实发货日期", null=True, blank=True
    )  # 实发货日期
    remarks = models.TextField(blank=True, null=True, verbose_name="备注")  # 备注
    actual_payment_received = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="实际收款金额", default=0.0
    )  # 实际收款金额
    status = models.CharField(
        max_length=10,
        choices=ORDER_STATUS_CHOICES,
        default="pending",
        verbose_name="订单状态",
    )  # 订单状态
    preparation_status = models.CharField(
        max_length=20,
        choices=PREPARATION_STATUS_CHOICES,
        default="not_started",
        verbose_name="备货状态",
    )  # 备货状态
    freight_cost_received = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="所收运费", default=0.0
    )  # 所收运费
    actual_freight_cost = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="实际运费", default=0.0
    )  # 实际运费
    tracking_number = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="运单号"
    )  # 运单号
    shipping_method = models.ForeignKey(
        "ShippingMethod", on_delete=models.SET_NULL, null=True, verbose_name="发货方式"
    )  # 发货方式
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="创建者",
    )  # 创建者
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="创建时间"
    )  # 创建时间
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="更新时间"
    )  # 更新时间

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name = "订单"
        verbose_name_plural = "订单"


############# 订单项模型 #############


class OrderItem(models.Model):
    # 价格类型选择
    PRICE_TYPE_CHOICES = [
        ("price_one", "价格一"),
        ("price_two", "价格二"),
    ]

    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.CASCADE, verbose_name="订单"
    )  # 订单
    product = models.ForeignKey(
        "Product", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="产品"
    )  # 产品
    flower_material = models.ForeignKey(
        "FlowerMaterial",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="花材",
    )  # 花材
    quantity = models.PositiveIntegerField(default=1, verbose_name="数量")  # 数量
    price_type = models.CharField(
        max_length=10,
        choices=PRICE_TYPE_CHOICES,
        default="price_one",
        verbose_name="价格类型",
    )  # 价格类型
    unit_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="单价", editable=False
    )  # 单价
    total_price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="总价", editable=False
    )  # 总价

    def save(self, *args, **kwargs):
        if self.product:
            self.unit_price = self.product.price  # 使用产品价格
        elif self.flower_material:
            if self.price_type == "price_one":
                self.unit_price = self.flower_material.price_one  # 使用花材价格一
            elif self.price_type == "price_two":
                self.unit_price = self.flower_material.price_two  # 使用花材价格二
        self.total_price = self.unit_price * self.quantity  # 总价 = 单价 * 数量
        super().save(*args, **kwargs)

    def __str__(self):
        if self.product:
            return f"{self.order.order_number} - {self.product.chinese_name}"
        elif self.flower_material:
            return f"{self.order.order_number} - {self.flower_material.chinese_name}"
        else:
            return f"{self.order.order_number} - 未知商品"

    class Meta:
        verbose_name = "订单项"
        verbose_name_plural = "订单项"


############# 订单利润统计模型 #############


class OrderProfit(models.Model):
    order = models.OneToOneField(
        Order, related_name="profit", on_delete=models.CASCADE, verbose_name="订单"
    )  # 订单
    theoretical_profit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="理论利润",
        editable=False,
        default=0.0,
    )  # 理论利润
    actual_profit = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="实际利润",
        editable=False,
        default=0.0,
    )  # 实际利润

    def calculate_profit(self):
        # 计算利润
        total_cost = Decimal(0.0)
        total_revenue = Decimal(0.0)
        for item in self.order.items.all():
            if item.product:
                total_cost += item.product.cost * item.quantity  # 计算产品总成本
                total_revenue += item.unit_price * item.quantity  # 计算产品总收入
            elif item.flower_material:
                total_cost += (
                    item.flower_material.cost_price * item.quantity
                )  # 计算花材总成本
                total_revenue += item.unit_price * item.quantity  # 计算花材总收入
        self.theoretical_profit = (
            total_revenue - total_cost + self.order.freight_cost_received
        )  # 计算理论利润（包含所收运费）
        self.actual_profit = (
            self.order.actual_payment_received
            - total_cost
            - self.order.actual_freight_cost
        )  # 计算实际利润（包含实际运费）

    def save(self, *args, **kwargs):
        self.calculate_profit()  # 保存前计算利润
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.order.order_number} - 利润"

    class Meta:
        verbose_name = "订单利润"
        verbose_name_plural = "订单利润"
