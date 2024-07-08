# Myflowers/urls.py

from django.contrib import admin
from django.urls import path
from app01 import views
from app01.views import base_view, home_view, control_panel_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),  # 将根URL指向home
    path("home/", home_view, name="home"),
    path("base/", base_view, name="base"),
    path("control-panel/", control_panel_view, name="control-panel"),
    path("flower-materials/", views.flower_materials_view, name="flower_materials"),
]
