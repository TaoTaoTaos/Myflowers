from django.core.management.base import BaseCommand
from django.utils import timezone
from app01.models import Product, FlowerMaterial


class Command(BaseCommand):
    help = "Update default updated_at fields to current time"

    def handle(self, *args, **kwargs):
        default_updated_at = "updated_at"

        # 更新所有花材的 updated_at 字段
        flowers = FlowerMaterial.objects.filter(updated_at__exact=default_updated_at)
        for flower in flowers:
            flower.updated_at = timezone.now()
            flower.save()

        self.stdout.write(self.style.SUCCESS("Successfully updated updated_at fields"))
