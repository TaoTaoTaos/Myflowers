from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import FlowerMaterial
from .forms import FlowerMaterialForm
from django.shortcuts import render, redirect
from .models import Category, Color, Process, Supplier, FlowerMaterial
from .forms import FlowerMaterialForm
from django.contrib import messages


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


# views.py

from django.shortcuts import render, get_object_or_404, redirect


def home_view(request):
    return render(request, "home.html")


def base_view(request):
    return render(request, "base.html")


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


# 添加花材


def flower_material_create(request):
    if request.method == "POST":
        form = FlowerMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "花材添加成功")
            return redirect("flower_material_list")
        else:
            # 如果表单验证失败，将错误信息添加到消息框中显示给用户
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
