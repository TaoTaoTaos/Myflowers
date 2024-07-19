from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import FlowerMaterial, Product
from .forms import FlowerMaterialForm
from django.shortcuts import render, redirect
from .models import (
    Category,
    Color,
    Process,
    Supplier,
    FlowerMaterial,
    Grade,
)
from .forms import FlowerMaterialForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


##########################普通视图#############################
@login_required(login_url="/login/")
def home_view(request):
    return render(request, "home.html", {"current_user": request.user})


def base_view(request):
    return render(request, "base.html", {"current_user": request.user})


def login_view(request):
    return render(request, "login.html", {"current_user": request.user})


def logout_view(request):
    logout(request)
    return redirect("home", {"current_user": request.user})


def control_panel_view(request):
    return render(request, "control_panel.html", {"current_user": request.user})


def QuoteMOD_view(request):
    return render(request, "QuoteMOD.html", {"current_user": request.user})


def success_page(request):
    return render(request, "success.html")


##########################普通视图END##############################

#########################注册登录############################
# 注册
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # 这里将用户数据保存到数据库中
            username = form.cleaned_data.get("username")
            messages.success(request, f"账号创建成功，您现在可以登录！")
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "register.html", {"form": form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomAuthenticationForm


# 登录
def login_view(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # 登录成功后的重定向
                return redirect("home")  # 替换成你的首页URL名称
    else:
        form = CustomAuthenticationForm()

    return render(request, "login.html", {"form": form})


#########################注册登录END############################
##########################花材###############################

from .forms import FlowerMaterialForm


@login_required
def add_flower_material(request):
    if request.method == "POST":
        form = FlowerMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            flower_material = form.save(commit=False)
            flower_material.created_by = request.user  # 将创建者设置为当前用户
            flower_material.save()
            return redirect("flower_material_list")  # 替换为你的重定向URL
    else:
        form = FlowerMaterialForm()
    return render(request, "add_flower_material.html", {"form": form})


# 花材表显示
def flower_materials_list(request):
    flower_materials = FlowerMaterial.objects.all()
    return render(
        request,
        "flower_material_list.html",
        {"flower_materials": flower_materials, "current_user": request.user},
    )


# 花材详情页
def flower_material_detail(request, model):
    material = get_object_or_404(FlowerMaterial, model=model)
    flower_materials = FlowerMaterial.objects.all()
    return render(
        request,
        "flower_material_detail.html",
        {
            "material": material,
            "flower_materials": flower_materials,
            "current_user": request.user,
        },
    )


# 花材编辑
def edit_flower_material(request, model):
    material = get_object_or_404(FlowerMaterial, model=model)
    if request.method == "POST":
        form = FlowerMaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            # 首先，使用 commit=False 保存表单，以获取更新但尚未保存的实例
            flower_material = form.save(commit=False)
            # 更新创建者字段
            flower_material.created_by = request.user
            # 最后，将更新的实例保存到数据库
            flower_material.save()
            return redirect("flower_material_detail", model=material.model)
    else:
        form = FlowerMaterialForm(instance=material)

    categories = Category.objects.all()
    colors = Color.objects.all()
    processes = Process.objects.all()
    suppliers = Supplier.objects.all()
    grades = Grade.objects.all()
    flower_materials = FlowerMaterial.objects.all()

    context = {
        "form": form,
        "material": material,
        "categories": categories,
        "colors": colors,
        "processes": processes,
        "suppliers": suppliers,
        "grades": grades,
        "flower_materials": flower_materials,
        "current_user": request.user,
    }

    return render(request, "flower_material_edit.html", context)


# 花材删除
from django.shortcuts import get_object_or_404, redirect, render


def delete_flower_material(request, model):
    material = get_object_or_404(FlowerMaterial, model=model)
    if request.method == "POST":
        material.delete()
        return redirect("flower_material_list")  # 重定向到花材列表页
    return render(
        request, "flower_material_confirm_delete.html", {"material": material}
    )


##########################花材end###############################


###############################产品####################################
from django.db import transaction, IntegrityError
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.forms import modelform_factory
from .models import Product, FlowerMaterial, ProductMaterial
from django.contrib.auth.decorators import login_required
from django.utils import timezone


@login_required
def add_product(request):
    # 使用 modelform_factory 创建 Product 表单，不包含 'materials', 'created_by', 'created_at', 'updated_at'
    ProductForm = modelform_factory(
        Product, exclude=["materials", "created_by", "created_at", "updated_at"]
    )

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)  # 添加 request.FILES
        if form.is_valid():
            try:
                with transaction.atomic():
                    product = form.save(commit=False)
                    product.created_by = request.user
                    product.created_at = timezone.now()
                    product.updated_at = timezone.now()
                    product.save()

                    # 处理花材信息
                    flower_materials = request.POST.get("flower_materials", "").split(
                        ";"
                    )
                    for fm in flower_materials:
                        if fm:  # 检查 fm 是否为空字符串
                            flower_material_model, quantity, ratio, price_type = (
                                fm.split(",")
                            )
                            flower_material = FlowerMaterial.objects.get(
                                model=flower_material_model
                            )
                            ProductMaterial.objects.create(
                                product=product,
                                flower_material=flower_material,
                                quantity=quantity,
                                ratio=ratio,
                                price_type=price_type,
                            )

                    return redirect("product_list")  # 重定向到一个成功页面
            except IntegrityError:
                form.add_error(None, "保存产品时出现错误，请重试。")
            except FlowerMaterial.DoesNotExist:
                form.add_error(None, "指定的花材不存在，请检查输入。")
    else:
        form = ProductForm()
        flower_materials = FlowerMaterial.objects.all()

    return render(
        request,
        "add_product.html",
        {"form": form, "flower_materials": flower_materials},
    )


########################
def success_page(request):
    return render(request, "success.html")


#################
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})


def product_details(request, model):
    product = get_object_or_404(Product, model=model)
    materials = product.productmaterial_set.all()

    context = {"product": product, "materials": materials}
    return render(request, "product_details.html", context)


##########################产品END#######################
