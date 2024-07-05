from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Product
from .forms import ProductForm


class ProductView(View):
    def get(self, request, id=None):
        if id:
            product = get_object_or_404(Product, id=id)
            form = ProductForm(instance=product)
        else:
            form = ProductForm()
        products = Product.objects.all()
        return render(request, "Product.html", {"form": form, "products": products})

    def post(self, request, id=None):
        if id:
            product = get_object_or_404(Product, id=id)
            form = ProductForm(request.POST, request.FILES, instance=product)
        else:
            form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Product")
        else:
            products = Product.objects.all()
            return render(request, "Product.html", {"form": form, "products": products})

    def delete(self, request, id):
        product = get_object_or_404(Product, id=id)
        product.delete()
        return redirect("Product")
