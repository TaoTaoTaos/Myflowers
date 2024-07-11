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
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, default=None
    )
    model = models.CharField(max_length=100, null=True, blank=False, default="")
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


class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
