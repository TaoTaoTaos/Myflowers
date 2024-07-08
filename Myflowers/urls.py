# Myflowers/urls.py

from django.contrib import admin
from django.urls import path
from app01 import views
from app01.views import index_view, base_view, home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),  # 将根URL指向home
    path("base/", base_view, name="base"),
    path("index/", index_view, name="index"),
    path("flower-materials/", views.flower_materials_view, name="flower_materials"),
    #
]
