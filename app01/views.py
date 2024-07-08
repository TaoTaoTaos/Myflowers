from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import FlowerMaterial
from .forms import FlowerMaterialForm

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


# 添加花材
def flower_material_create(request):
    if request.method == "POST":
        form = FlowerMaterialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("flower_material_list")
    else:
        form = FlowerMaterialForm()
    return render(request, "flower_material_form.html", {"form": form})


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
