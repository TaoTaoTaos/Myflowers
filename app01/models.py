from django.db import models


class Product(models.Model):
    # 产品型号
    model = models.CharField(max_length=200)
    # 产品图片
    picture = models.ImageField(upload_to="products/")
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

    ######################################################################
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
