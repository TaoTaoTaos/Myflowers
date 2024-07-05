from django.shortcuts import render, redirect
from django.views import View
from .models import Product
from .forms import ProductForm


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "products.html", {"products": products})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("products")
        else:
            return render(request, "products.html", {"form": form})
