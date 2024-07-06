from django.db import models


class Product(models.Model):
    # 自增编号
    id = models.AutoField(primary_key=True)
    # 产品型号
    model = models.CharField(max_length=200)
    # 产品图片
    picture = models.ImageField(upload_to="products_picture/")
    # 产品规格(复杂)
    specification = models.TextField()  # TextField存储大段文本

    # 产品颜色
    COLOR_CHOICES = [
        ("red", "红色"),
        ("blue", "蓝色"),
        ("green", "绿色"),
        # 更多颜色...
    ]
    COLOR = models.CharField(max_length=200, choices=COLOR_CHOICES)

    # 产品数量
    qty = models.IntegerField()
    # 产品单价
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    # 产品总价
    amount = models.DecimalField(max_digits=6, decimal_places=2)

    def save(self, *args, **kwargs):
        self.amount = self.unit_price * self.qty
        super().save(*args, **kwargs)

    ######################################################################


class RawMaterial(models.Model):
    # 自增编号
    id = models.AutoField(primary_key=True)
    # 花材、资材
    material = models.CharField(max_length=200)
    # 型号
    model = models.CharField(max_length=200)
    # 重量
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    # 生产方式
    PROCESS_CHOICES = [
        ("drying", "干燥"),
        ("dyeing", "染色"),
        ("drying_and_dyeing", "干燥和染色"),
        ("bleaching", "漂"),
        # 更多生产方式...
    ]
    process = models.CharField(max_length=200, choices=PROCESS_CHOICES)
    # 包装规格
    packing_dimension = models.CharField(max_length=200)
    # 包装数量
    packing_qty = models.IntegerField()
    # 购买时规格
    purchase_spe = models.CharField(max_length=200)
    # 使用时的规格
    usage_spe = models.CharField(max_length=200)
    # 等级
    grade = models.CharField(max_length=200)
    # 供应商
    supplier = models.CharField(max_length=200)
    # 库存
    stock = models.IntegerField()
    # 尺寸
    size = models.CharField(max_length=200)
