# Generated by Django 5.0.7 on 2024-07-24 06:35

import app01.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app01", "0012_customer_updated_at_followuprecord"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="followuprecord",
            name="attachment",
        ),
        migrations.AlterField(
            model_name="followuprecord",
            name="created_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="followuprecord",
            name="follow_up_time",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name="FollowUpAttachment",
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
                ("file", models.FileField(upload_to=app01.models.user_directory_path)),
                (
                    "follow_up_record",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="attachments",
                        to="app01.followuprecord",
                    ),
                ),
            ],
        ),
    ]