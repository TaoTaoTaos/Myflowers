# Myflowers/urls.py

from django.contrib import admin
from django.urls import path
from app01 import views
from app01.views import base_view, home_view, control_panel_view

from app01.views import (
    flower_material_create,
    flower_materials_list,
    flower_material_update,
    flower_material_delete,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_view, name="home"),  # 将根URL指向home
    path("home/", home_view, name="home"),
    path("base/", base_view, name="base"),
    path("control-panel/", control_panel_view, name="control-panel"),
    path(
        "/flower_material_create/",
        flower_material_create,
        name="flower_material_create",
    ),  # 花材增
    path(
        "flower-materials/<int:pk>/update/",
        flower_material_update,
        name="flower_material_update",
    ),  # 花材改
    path(
        "flower-materials/<int:pk>/delete/",
        flower_material_delete,
        name="flower_material_delete",
    ),  # 花材删
    path(
        "flower-materials/", flower_materials_list, name="flower_material_list"
    ),  # 花材查
    ################################################################
]
