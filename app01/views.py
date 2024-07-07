from django.views.generic import ListView
from .models import FlowerMaterial
from django.shortcuts import render
from django.shortcuts import render
from .models import FlowerMaterial


def flower_materials_view(request):
    flower_materials = FlowerMaterial.objects.all()
    return render(
        request, "flower_materials.html", {"flower_materials": flower_materials}
    )


def index_view(request):
    return render(request, "index.html")


class FlowerMaterialListView(ListView):
    model = FlowerMaterial
    template_name = "flower_material_list.html"
    context_object_name = "flower_materials"
    paginate_by = 15  # 每页显示15条记录
