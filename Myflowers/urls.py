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
    ############################### 包装 ###############################
    path("add_packaging/", add_packaging, name="add_packaging"),
    path("packaging_list/", packaging_list, name="packaging_list"),
    path("edit_packaging/<str:pk>/", edit_packaging, name="edit_packaging"),
    path("delete_packaging/<str:pk>/", delete_packaging, name="delete_packaging"),
    ############################### 包装 END ###############################
    ############################### 管理员 ###############################
    path("admin/", admin.site.urls),
    ############################### 管理员 END ###############################
    ############################### 基础和主页 ###############################
    path("base/", base_view, name="base"),
    path("home/", home_view, name="home"),
    ############################### 基础和主页 END ###############################
    ############################### 认证 ###############################
    path("", login_view, name="login"),  # 默认打开网页指向登录页面
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", register_view, name="register"),
    ############################### 认证 END ###############################
    ############################### 用户个人资料 ###############################
    path("profile/", profile_view, name="profile"),
    path("set_background/", set_background, name="set_background"),
    ############################### 用户个人资料 END ###############################
    ############################### 超级用户 ###############################
    path("superuser_page/", superuser_page, name="superuser_page"),
    ############################### 超级用户 END ###############################
    ############################### 评论 ###############################
    path("add_comment/", views.add_comment_view, name="add_comment"),
    path(
        "delete_comment/<int:comment_id>/", delete_comment_view, name="delete_comment"
    ),
    ############################### 评论 END ###############################
    ############################### 控制面板 ###############################
    path("control-panel/", control_panel_view, name="control-panel"),
    ############################### 控制面板 END ###############################
    ############################### 产品 ###############################
    path("add_product/", add_product, name="add_product"),
    path("product_list/", product_list, name="product_list"),
    path("product_details/<str:model>/", product_details, name="product_details"),
    path("products/edit/<str:model>/", views.edit_product, name="edit_product"),
    path("product_details/<str:model>/edit/", views.edit_product, name="edit_product"),
    path("product_details/<str:model>/", views.product_details, name="product_details"),
    path("product_detail/<str:model>/", views.product_details, name="product_detail"),
    path("products/delete/<str:model>/", views.delete_product, name="delete_product"),
    ############################### 产品 END ###############################
    ############################### 花材 ###############################
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
    ############################### 花材 END ###############################
    ############################### 报价 ###############################
    path("add_quote_item/", add_quote_item, name="add_quote_item"),
    path("save_quote/", save_quote, name="save_quote"),
    ############################### 报价 END ###############################
    ############################### 客户 ###############################
    path("customer_list/", customer_list, name="customer_list"),
    path("add_customer/", add_customer, name="add_customer"),
    path(
        "customers/<str:customer_id>/follow-ups/", follow_up_list, name="follow_up_list"
    ),
    path(
        "customers/<str:customer_id>/update/",
        views.customer_update,
        name="customer_update",
    ),
    ############################### 客户 END ###############################
    ############################### 成功页面 ###############################
    path("success/", success_page, name="success_page"),
    ############################### 成功页面 END ###############################
    ############################### 订单 ###############################
    path(
        "order_create/", OrderCreateView.as_view(), name="order_create"
    ),  # 确保使用 .as_view()
    path("order_list/", views.order_list, name="order_list"),
    path("order_list/<int:order_id>/", views.order_details, name="order_details"),
    path("order_list/<int:order_id>/edit/", views.order_edit, name="order_edit"),
    path("order_list/<int:order_id>/delete/", views.delete_order, name="delete_order"),
    ############################### 订单 END ###############################
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
