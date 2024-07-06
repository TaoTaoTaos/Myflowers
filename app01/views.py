from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product
from .forms import ProductForm
from django.contrib import messages


# 首页
def index(request):
    return render(request, "index.html")


# def add_product(request):
# return render(request, "add_product.html")


from django.shortcuts import render, redirect
from .models import Product


# 新增商品函數
def add_product(request):
    if request.method == "POST":
        model = request.POST.get("model")
        picture = request.FILES.get("picture")
        specification = request.POST.get("specification")
        color = request.POST.get("color")
        qty = int(request.POST.get("qty"))
        unit_price = float(request.POST.get("unit_price"))

        product = Product(
            model=model,
            picture=picture,
            specification=specification,
            COLOR=color,
            qty=qty,
            unit_price=unit_price,
        )
        product.save()
        messages.success(request, "商品添加成功！")  # 添加成功消息

        return redirect("/add")  # 重定向到商品列表页面

    return render(request, "add_product.html")  # 渲染商品添加页面


def product_list(request):
    products = Product.objects.all()
    return render(request, "product_list.html", {"products": products})
