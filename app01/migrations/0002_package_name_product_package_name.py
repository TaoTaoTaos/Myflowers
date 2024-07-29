# Generated by Django 5.0.7 on 2024-07-29 03:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app01", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="package_name",
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
                (
                    "name",
                    models.CharField(
                        choices=[("OOP Bag", "OOP Bag")], max_length=100, unique=True
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="product",
            name="package_name",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app01.package_name",
            ),
        ),
    ]