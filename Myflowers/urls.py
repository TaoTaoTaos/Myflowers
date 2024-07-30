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
    set_background,
    delete_comment_view,
    add_packaging,
    packaging_list,
    edit_packaging,
    delete_packaging,
    OrderCreateView,
)

urlpatterns = [
    path("add_packaging/", add_packaging, name="add_packaging"),
    path("packaging_list/", packaging_list, name="packaging_list"),
    path("edit_packaging/<str:pk>/", edit_packaging, name="edit_packaging"),
    path("delete_packaging/<str:pk>/", delete_packaging, name="delete_packaging"),
    # Admin URL
    path("admin/", admin.site.urls),
    # Base and Home URLs
    path("base/", base_view, name="base"),
    path("home/", home_view, name="home"),
    # Authentication URLs
    path("", login_view, name="login"),  # 默认打开网页指向登录页面
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    # User Profile URLs
    path("profile/", profile_view, name="profile"),
    path("set_background/", set_background, name="set_background"),
    # Superuser Page URL
    path("superuser_page/", superuser_page, name="superuser_page"),
    # Comment URLs
    path("add_comment/", views.add_comment_view, name="add_comment"),
    path(
        "delete_comment/<int:comment_id>/", delete_comment_view, name="delete_comment"
    ),
    # Control Panel URL
    path("control-panel/", control_panel_view, name="control-panel"),
    # Product URLs
    path("add_product/", add_product, name="add_product"),
    path("product_list/", product_list, name="product_list"),
    path("product_details/<str:model>/", product_details, name="product_details"),
    path("products/edit/<str:model>/", views.edit_product, name="edit_product"),
    path("product_details/<str:model>/edit/", views.edit_product, name="edit_product"),
    path("product_details/<str:model>/", views.product_details, name="product_details"),
    # 添加这一行以定义 product_detail 的 URL 模式
    path("product_detail/<str:model>/", views.product_details, name="product_detail"),
    path("products/delete/<str:model>/", views.delete_product, name="delete_product"),
    # Flower Material URLs
    path(
        "flower_material/<str:model>/",
        flower_material_detail,
        name="flower_material_detail",
    ),  # 花材详情
    path(
        "add-flower-material/", views.add_flower_material, name="add_flower_material"
    ),  # 花材增
    path(
        "edit/<str:model>/", edit_flower_material, name="edit_flower_material"
    ),  # 花材改
    path(
        "delete/<str:model>/", delete_flower_material, name="delete_flower_material"
    ),  # 花材删
    path(
        "flower-materials/", flower_materials_list, name="flower_material_list"
    ),  # 花材查
    # Quote URLs
    path("add_quote_item/", add_quote_item, name="add_quote_item"),
    path("save_quote/", save_quote, name="save_quote"),
    # Customer URLs
    path("customer_list/", customer_list, name="customer_list"),
    path("add_customer/", add_customer, name="add_customer"),
    path(
        "customers/<str:customer_id>/follow-ups/", follow_up_list, name="follow_up_list"
    ),
    # Success Page URL
    path("success/", success_page, name="success_page"),
    ###############################
    path(
        "order_create/", OrderCreateView.as_view(), name="order_create"
    ),  # 确保使用 .as_view()
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
