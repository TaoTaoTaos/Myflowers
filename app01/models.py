from django.db import models


class Supplier(models.Model):
    name = models.CharField("供应商名称", max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "供应商"
        verbose_name_plural = "供应商"

    def __str__(self):
        return self.name


class Series(models.Model):
    name = models.CharField("系列名称", max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "系列"
        verbose_name_plural = "系列"

    def __str__(self):
        return self.name


class Process(models.Model):
    name = models.CharField("生产方式名称", max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "生产方式"
        verbose_name_plural = "生产方式"

    def __str__(self):
        return self.name


class FlowerMaterial(models.Model):
    series = models.ForeignKey(Series, on_delete=models.CASCADE, verbose_name="系列")
    model = models.CharField("型号", max_length=50, unique=True)
    name = models.CharField("品名", max_length=100)
    size = models.CharField("尺寸", max_length=50)
    weight = models.DecimalField("重量", max_digits=10, decimal_places=2)
    process = models.ForeignKey(
        Process, on_delete=models.CASCADE, verbose_name="生产方式"
    )
    packing_dimension = models.CharField("包装规格", max_length=100)
    packing_qty = models.IntegerField("包装数量")
    purchase_spe = models.CharField("购买时的规格", max_length=100)
    usage_spe = models.CharField("使用时的规格", max_length=100)
    grade = models.CharField("等级", max_length=50)
    stock = models.IntegerField("库存")

    class Meta:
        ordering = ["name"]
        verbose_name = "花材"
        verbose_name_plural = "花材"

    def __str__(self):
        return self.name


class SupplierPrice(models.Model):
    supplier = models.ForeignKey(
        Supplier, on_delete=models.CASCADE, verbose_name="供应商"
    )
    flower_material = models.ForeignKey(
        FlowerMaterial, on_delete=models.CASCADE, verbose_name="花材"
    )
    price = models.DecimalField("价格", max_digits=10, decimal_places=2)

    class Meta:
        unique_together = ("supplier", "flower_material")
        verbose_name = "供应商价格"
        verbose_name_plural = "供应商价格"

    def __str__(self):
        return f"{self.supplier.name} - {self.flower_material.name} - {self.price}"
