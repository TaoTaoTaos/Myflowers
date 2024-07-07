from django.views.generic import ListView
from .models import FlowerMaterial
from django.shortcuts import render


def index_view(request):
    return render(request, "index.html")


class FlowerMaterialListView(ListView):
    model = FlowerMaterial
    template_name = "flower_material_list.html"
    context_object_name = "flower_materials"
    paginate_by = 15  # 每页显示15条记录
