# Generated by Django 5.0.7 on 2024-07-24 05:55

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app01", "0011_alter_customer_address_alter_customer_customer_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name="FollowUpRecord",
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
                    "follow_up_time",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
                ("follow_up_count", models.PositiveIntegerField()),
                ("details", models.TextField()),
                (
                    "attachment",
                    models.FileField(
                        blank=True, null=True, upload_to="follow_up_attachments/"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="follow_up_records",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="follow_ups",
                        to="app01.customer",
                    ),
                ),
            ],
        ),
    ]
