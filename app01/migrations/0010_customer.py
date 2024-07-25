# Generated by Django 5.0.7 on 2024-07-24 05:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app01", "0009_remove_productmaterial_price_type_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_id", models.CharField(max_length=100, unique=True)),
                ("name", models.CharField(max_length=100)),
                ("country", models.CharField(max_length=100)),
                ("company_name", models.CharField(max_length=100)),
                ("address", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=20)),
                ("mobile", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("sales_channel", models.CharField(max_length=100)),
                ("product_demand", models.CharField(max_length=255)),
                ("source", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[("已成交", "已成交"), ("跟进中", "跟进中")], max_length=10
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="customers",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]