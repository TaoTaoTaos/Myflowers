# Myflowers/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app01 import views
from app01.views import (
    base_view,
    home_view,
    control_panel_view,
    login_view,
    register_view,
    logout_view,
    add_product,
    products_list,
    QuoteMOD_view,
)

from app01.views import (
    edit_flower_material,
    flower_materials_list,
    delete_flower_material,
    products_list,
    flower_material_detail,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("base/", base_view, name="base"),
    #############################################
    path("", login_view, name="login"),  # 打开网页指向home
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("home/", home_view, name="home"),
    path("control-panel/", control_panel_view, name="control-panel"),
    path("register/", register_view, name="register"),
    path("product_list/", products_list, name="product_list"),
    path("add_product/", add_product, name="add_product"),
    path("QuoteMOD/", views.QuoteMOD_view, name="QuoteMOD"),
    ####################花材######################
    path(
        "add-flower-material/", views.add_flower_material, name="add_flower_material"
    ),  # 花材增
    path(
        "edit/<str:model>/", views.edit_flower_material, name="edit_flower_material"
    ),  # 花材改
    path(
        "delete/<str:model>/",
        views.delete_flower_material,
        name="delete_flower_material",
    ),  # 花材删
    path(
        "flower-materials/", flower_materials_list, name="flower_material_list"
    ),  # 花材查
    path(
        "flower_material/<str:model>/",
        views.flower_material_detail,
        name="flower_material_detail",
    ),
    ####################花材END######################
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
