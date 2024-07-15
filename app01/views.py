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
    CreatedBy,
    Grade,
)
from .forms import FlowerMaterialForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

##########################

from .forms import FlowerMaterialForm


def add_flower_material(request):
    if request.method == "POST":
        form = FlowerMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            flower_material = form.save(commit=False)

            # 设置默认值

            if not flower_material.chinese_name:
                flower_material.chinese_name = "默认名"
            if not flower_material.english_name:
                flower_material.english_name = "Default Name"
            if not flower_material.scientific_name:
                flower_material.scientific_name = "Default Scientific Name"

            if not flower_material.size:
                flower_material.size = 0.0
            if not flower_material.weight:
                flower_material.weight = 0.0
            if not flower_material.sale_spec_quantity:
                flower_material.sale_spec_quantity = 1
            if not flower_material.outer_box_length:
                flower_material.outer_box_length = 0.0
            if not flower_material.outer_box_width:
                flower_material.outer_box_width = 0.0
            if not flower_material.outer_box_height:
                flower_material.outer_box_height = 0.0
            if not flower_material.packing_quantity:
                flower_material.packing_quantity = 1

            if not flower_material.price_one:
                flower_material.price_one = 0.0
            if not flower_material.price_two:
                flower_material.price_two = 0.0

            form.save()
            messages.success(request, "花材添加成功")
            return redirect("flower_material_list")
        else:
            messages.error(request, "花材添加失败，（类别、型号、操作人；为必填项）")
    else:
        form = FlowerMaterialForm()

    categories = Category.objects.all()
    grades = Grade.objects.all()
    processes = Process.objects.all()
    suppliers = Supplier.objects.all()
    Created_bys = CreatedBy.objects.all()

    context = {
        "form": form,
        "categories": categories,
        "processes": processes,
        "grades": grades,
        "suppliers": suppliers,
        "Created_bys": Created_bys,
    }
    return render(
        request,
        "add_flower_material.html",
        context,
    )


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


# 花材表显示
def flower_materials_list(request):
    flower_materials = FlowerMaterial.objects.all()
    return render(
        request,
        "flower_material_list.html",
        {"flower_materials": flower_materials, "current_user": request.user},
    )


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


def products_list(request):
    products = Product.objects.all()
    return render(
        request,
        "product_list.html",
        {"products": products, "current_user": request.user},
    )


from django.shortcuts import render, redirect
from .forms import FlowerMaterialForm


def edit_flower_material(request, model):
    material = get_object_or_404(FlowerMaterial, model=model)
    if request.method == "POST":
        form = FlowerMaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            form.save()
            return redirect("flower_material_list")  # 重定向到花材列表页
    else:
        form = FlowerMaterialForm(instance=material)
    return render(request, "edit_flower_material.html", {"form": form})


def delete_flower_material(request, model):
    material = get_object_or_404(FlowerMaterial, model=model)
    if request.method == "POST":
        material.delete()
        return redirect("flower_material_list")  # 重定向到花材列表页
    return render(
        request, "flower_material_confirm_delete.html", {"material": material}
    )


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


# 添加产品
from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from .forms import (
    ProductForm,
    ProductMaterialForm,
)  # 导入 ProductForm 和 ProductMaterialForm
from .models import ProductMaterial


def add_product(request):
    ProductMaterialFormSet = modelformset_factory(
        ProductMaterial, form=ProductMaterialForm, extra=1
    )

    if request.method == "POST":
        product_form = ProductForm(request.POST)
        material_formset = ProductMaterialFormSet(
            request.POST, queryset=ProductMaterial.objects.none()
        )

        if product_form.is_valid() and material_formset.is_valid():
            product = product_form.save()

            for form in material_formset:
                material = form.save(commit=False)
                material.product = product
                material.save()

            return redirect("product_list")  # 重定向到产品列表页面或其他页面
    else:
        product_form = ProductForm()
        material_formset = ProductMaterialFormSet(
            queryset=ProductMaterial.objects.none()
        )

    context = {
        "product_form": product_form,
        "material_formset": material_formset,
    }

    return render(request, "add_product.html", context)
