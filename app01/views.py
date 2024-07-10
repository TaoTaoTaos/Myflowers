from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import FlowerMaterial
from .forms import FlowerMaterialForm
from django.shortcuts import render, redirect
from .models import Category, Color, Process, Supplier, FlowerMaterial
from .forms import FlowerMaterialForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

##########################


def add_flower_material(request):
    if request.method == "POST":
        form = FlowerMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "花材添加成功")
            return redirect("flower_material_list")
        else:
            messages.error(request, "花材添加失败，请检查表单内容")
    else:
        form = FlowerMaterialForm()

    categories = Category.objects.all()
    colors = Color.objects.all()
    processes = Process.objects.all()
    suppliers = Supplier.objects.all()

    context = {
        "form": form,
        "categories": categories,
        "colors": colors,
        "processes": processes,
        "suppliers": suppliers,
    }
    return render(request, "add_flower_material.html", context)


@login_required(login_url="/login/")
def home_view(request):
    return render(request, "home.html")


def base_view(request):
    return render(request, "base.html")


def login_view(request):
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("home")


def control_panel_view(request):
    return render(request, "control_panel.html")


# 花材表显示
def flower_materials_list(request):
    flower_materials = FlowerMaterial.objects.all()
    return render(
        request, "flower_material_list.html", {"flower_materials": flower_materials}
    )


from django.shortcuts import render, redirect
from .forms import FlowerMaterialForm


# 更新花材
def flower_material_update(request, pk):
    flower_material = get_object_or_404(FlowerMaterial, pk=pk)
    if request.method == "POST":
        form = FlowerMaterialForm(request.POST, instance=flower_material)
        if form.is_valid():
            form.save()
            return redirect("flower_material_list")
    else:
        form = FlowerMaterialForm(instance=flower_material)
    return render(request, "flower_material_form.html", {"form": form})


# 删除花材
def flower_material_delete(request, pk):
    flower_material = get_object_or_404(FlowerMaterial, pk=pk)
    if request.method == "POST":
        flower_material.delete()
        return redirect("flower_material_list")
    return render(
        request,
        "flower_material_confirm_delete.html",
        {"flower_material": flower_material},
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
