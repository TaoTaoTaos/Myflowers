from django.views.generic import ListView
from .models import FlowerMaterial
from django.shortcuts import render
from django.shortcuts import render
from .models import FlowerMaterial


def home_view(request):
    return render(request, "home.html")


def base_view(request):
    return render(request, "base.html")


def control_panel_view(request):
    return render(request, "control_panel.html")


def flower_materials_view(request):
    flower_materials = FlowerMaterial.objects.all()
    return render(
        request, "flower_material_list.html", {"flower_materials": flower_materials}
    )
