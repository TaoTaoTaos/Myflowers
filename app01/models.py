from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from decimal import Decimal
from django.conf import settings


class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Process(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


from datetime import datetime


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


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username


##############################产品#####################################
class Product(models.Model):
    model = models.CharField(
        max_length=100, blank=False, default="Product0000", primary_key=True
    )
    materials = models.ManyToManyField(FlowerMaterial, through="ProductMaterial")
    chinese_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200)

    ######################
    size = models.CharField(max_length=200, blank=True, default="0")
    weight = models.CharField(max_length=200, blank=True, default="0")
    color = models.CharField(max_length=200, blank=True, default="默认颜色")
    Package = models.CharField(max_length=200, blank=True, default="默认包装")
    sale_spec_quantity = models.CharField(
        max_length=200, help_text="销售规格的数字", blank=True, default=""
    )
    sale_spec_unit = models.CharField(
        max_length=10,
        help_text="销售规格的单位",
        choices=[("box", "box"), ("pcs", "pcs"), ("g", "g"), ("kg", "kg")],
        blank=True,
        null=True,
        default="box",
    )
    ###########################################################
    inner_box_long = models.FloatField(
        help_text="长度，单位：cm", null=True, blank=True, default=0.0
    )
    inner_box_width = models.FloatField(
        help_text="长度，单位：cm", null=True, blank=True, default=0.0
    )
    inner_box_height = models.FloatField(
        help_text="长度，单位：cm", null=True, blank=True, default=0.0
    )
    ##########################################################
    outer_box_length = models.FloatField(
        help_text="长度，单位：cm", null=True, blank=True, default=0.0
    )
    outer_box_width = models.FloatField(
        help_text="宽度，单位：cm", null=True, blank=True, default=0.0
    )
    outer_box_height = models.FloatField(
        help_text="高度，单位：cm", null=True, blank=True, default=0.0
    )
    ##########################################################
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    loss_rate = models.FloatField(default=0.0)

    @property
    def cost(self):
        total_cost = Decimal(0)
        for material in self.productmaterial_set.all():
            if material.price_type == "price_one":
                material_cost = (
                    material.flower_material.price_one
                    * Decimal(material.quantity)
                    * Decimal(material.ratio)
                )
            else:
                material_cost = (
                    material.flower_material.price_two
                    * Decimal(material.quantity)
                    * Decimal(material.ratio)
                )
            total_cost += material_cost
        total_cost += self.labor_cost
        total_cost *= Decimal(1 + self.loss_rate)
        return total_cost

    ##############################################################
    description = models.TextField(null=True, blank=True)  # 备注信息
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
        return (
            f"{self.inner_box_length} * {self.inner_box_width} * {self.inner_box_height} cm"
            if self.inner_box_length and self.inner_box_width and self.inner_box_height
            else ""
        )

    @property
    def outer_box_size(self):
        return (
            f"{self.outer_box_length} * {self.outer_box_width} * {self.outer_box_height} cm"
            if self.outer_box_length and self.outer_box_width and self.outer_box_height
            else ""
        )

    def __str__(self):
        return self.chinese_name


class ProductMaterial(models.Model):
    PRICE_TYPE_CHOICES = [
        ("price_one", "Price One"),
        ("price_two", "Price Two"),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    flower_material = models.ForeignKey(FlowerMaterial, on_delete=models.CASCADE)
    quantity = models.FloatField(default=1.0)
    ratio = models.FloatField(default=1.0)
    price_type = models.CharField(
        max_length=10, choices=PRICE_TYPE_CHOICES, default="price_one"
    )

    def __str__(self):
        return f"{self.product.chinese_name} - {self.flower_material.chinese_name} x {self.quantity} (Ratio: {self.ratio}, Price: {self.price_type})"
