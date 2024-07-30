import pandas as pd
from decimal import Decimal, InvalidOperation
from django.core.management.base import BaseCommand
from django.conf import settings
from django.contrib.auth import get_user_model
from app01.models import (
    Category,
    Color,
    Process,
    Supplier,
    FlowerMaterial,
    Grade,
)

User = get_user_model()


class Command(BaseCommand):
    help = "Import flower material data from Excel file"

    def handle(self, *args, **kwargs):
        df = pd.read_excel(r"F:\Myflowers\app01\management\commands\数据库表.xlsx")

        def to_decimal(value):
            """Convert value to decimal, return None if invalid."""
            try:
                return Decimal(value)
            except (InvalidOperation, TypeError, ValueError):
                return None

        for index, row in df.iterrows():
            # 获取或创建外键关联的对象
            category, _ = Category.objects.get_or_create(name=row["category"])
            color, _ = Color.objects.get_or_create(name=row["color"])
            process, _ = Process.objects.get_or_create(name=row["process"])
            supplier, _ = Supplier.objects.get_or_create(name=row["supplier"])
            grade, _ = Grade.objects.get_or_create(name=row["grade"])

            # 获取created_by字段的用户实例
            try:
                created_by = User.objects.get(username=row["created_by"])
            except User.DoesNotExist:
                created_by = None

            # 准备FlowerMaterial实例的字段
            flower_material_data = {
                "category": category,
                "chinese_name": row["chinese_name"],
                "english_name": row["english_name"],
                "scientific_name": row["scientific_name"],
                "color": color.name,  # 使用name字段
                "chineses_specifications": row["chineses_specifications"],
                "size": row["size"],
                "weight": row["weight"],
                "sale_spec_quantity": to_decimal(row["sale_spec_quantity"]),
                "sale_spec_unit": row["sale_spec_unit"],
                "process": process,
                "outer_box_length": to_decimal(row["outer_box_length"]),
                "outer_box_width": to_decimal(row["outer_box_width"]),
                "outer_box_height": to_decimal(row["outer_box_height"]),
                "packing_quantity": to_decimal(row["packing_quantity"]),
                "grade": grade,
                "supplier": supplier,
                "price_one": to_decimal(row["price_one"]),
                "price_two": to_decimal(row["price_two"]),
                "created_by": created_by,
            }

            # 确保不能为NULL的字段有有效值
            mandatory_fields = [
                "weight",
                "sale_spec_quantity",
                "outer_box_length",
                "outer_box_width",
                "outer_box_height",
                "packing_quantity",
                "price_one",
                "price_two",
            ]
            for field in mandatory_fields:
                if flower_material_data[field] is None:
                    flower_material_data[field] = Decimal(
                        0
                    )  # 或者设置为其他合理的默认值

            # 检查image字段
            if not pd.isna(row["image"]):
                flower_material_data["image"] = row["image"]

            # 使用 update_or_create 方法来创建或更新 FlowerMaterial 实例
            FlowerMaterial.objects.update_or_create(
                model=row["model"], defaults=flower_material_data
            )

        self.stdout.write(self.style.SUCCESS("Data imported successfully."))

        # manage.py import_flower_data
