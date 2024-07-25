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
    QuoteMOD_view,
    success_page,
    product_list,
    edit_flower_material,
    flower_materials_list,
    delete_flower_material,
    flower_material_detail,
    product_details,
    add_quote_item,
    save_quote,
    customer_list,
    add_customer,
    follow_up_list,
    superuser_page,
    profile_view,
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("base/", base_view, name="base"),
    path("superuser_page/", superuser_page, name="superuser_page"),
    path("profile/", profile_view, name="profile"),
    path("add_comment/", views.add_comment_view, name="add_comment"),
    #############################################
    path("", login_view, name="login"),  # 打开网页指向home
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("home/", home_view, name="home"),
    path("control-panel/", control_panel_view, name="control-panel"),
    path("register/", register_view, name="register"),
    path("add_product/", add_product, name="add_product"),
    path("success/", success_page, name="success_page"),
    ###############产品############
    path("product_list/", product_list, name="product_list"),
    path("product_details/<str:model>/", views.product_details, name="product_details"),
    path("products/edit/<str:model>/", views.edit_product, name="edit_product"),
    path("product_details/<str:model>/edit/", views.edit_product, name="edit_product"),
    path("products/delete/<str:model>/", views.delete_product, name="delete_product"),
    ############产品END############
    ####################花材######################
    path(
        "flower_material/<str:model>/",
        views.flower_material_detail,
        name="flower_material_detail",
    ),  # 花材详情
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
    ####################花材END######################
    ###################报价单#########################
    path("add_quote_item", add_quote_item, name="add_quote_item"),
    path("save_quote/", save_quote, name="save_quote"),
    ###################报价单#########################
    #############客户信息###########
    path("customer_list/", customer_list, name="customer_list"),
    path("add_customer/", add_customer, name="add_customer"),
    path(
        "customers/<str:customer_id>/follow-ups/", follow_up_list, name="follow_up_list"
    ),
    #############客户信息end###########
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
