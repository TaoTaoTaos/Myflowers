# models.py
from django.db import models
from django.contrib.auth.models import AbstractUser


class Grade(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Process(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CreatedBy(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


# 原材料类
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
    size = models.FloatField(help_text="单位：cm", blank=True, default=0.0)
    weight = models.FloatField(help_text="单位：g", blank=True, default=0.0)
    sale_spec_quantity = models.FloatField(help_text="数量", blank=True, default=0.0)
    sale_spec_unit = models.CharField(
        max_length=10,
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
        CreatedBy, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )

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


##################原材料END#################


##################用户信息#################
class CustomUser(AbstractUser):
    def __str__(self):
        return self.username


##################用户信息END#################


##################产品信息#################
from decimal import Decimal


class Product(models.Model):
    model = models.CharField(
        max_length=100, blank=False, default="Product0000", primary_key=True
    )
    description = models.TextField(null=True, blank=True)
    chinese_name = models.CharField(max_length=200)
    english_name = models.CharField(max_length=200)
    materials = models.ManyToManyField(FlowerMaterial, through="ProductMaterial")

    labor_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    loss_rate = models.FloatField(default=0.0)
    created_by = models.ForeignKey(
        CreatedBy, on_delete=models.SET_NULL, null=True, blank=True, default=None
    )

    def __str__(self):
        return self.chinese_name  # 修改为返回 Chinese name

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
        return f"{self.product.name} - {self.flower_material.chinese_name} x {self.quantity} (Ratio: {self.ratio}, Price: {self.price_type})"


##################产品信息END#################
