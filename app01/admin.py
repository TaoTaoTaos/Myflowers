from django.contrib import admin
from .models import Supplier, Series, Process, FlowerMaterial, SupplierPrice

admin.site.register(Supplier)
admin.site.register(Series)
admin.site.register(Process)
admin.site.register(FlowerMaterial)
admin.site.register(SupplierPrice)
