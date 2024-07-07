# Myflowers/urls.py

from django.contrib import admin
from django.urls import path
from app01 import views
from app01.views import FlowerMaterialListView, index_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index_view, name="home"),  # 将根URL指向index_view
    path("index/", index_view, name="home"),
    path("flower-materials/", views.flower_materials_view, name="flower_materials"),
    #
]
