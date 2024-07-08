from django.views.generic import ListView
from .models import FlowerMaterial
from django.shortcuts import render
from django.shortcuts import render
from .models import FlowerMaterial


def flower_materials_view(request):
    flower_materials = FlowerMaterial.objects.all()
    return render(
        request, "flower_material_list.html", {"flower_materials": flower_materials}
    )


def index_view(request):
    return render(request, "index.html")


def home_view(request):
    return render(request, "home.html")


def base_view(request):
    return render(request, "base.html")
