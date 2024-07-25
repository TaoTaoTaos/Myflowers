from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import FlowerMaterial, Product
from .forms import FlowerMaterialForm
from django.shortcuts import render, redirect
from .models import (
    Category,
    Color,
    Process,
    Supplier,
    FlowerMaterial,
    Grade,
)
from .forms import FlowerMaterialForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import user_passes_test


##########################普通视图#############################


def superuser_required(view_func):
    decorated_view_func = user_passes_test(lambda u: u.is_superuser)(view_func)
    return decorated_view_func


@superuser_required
def superuser_page(request):
    return render(request, "superuser.html", {"current_user": request.user})


from django.shortcuts import render
from .models import Product, FlowerMaterial


@login_required(login_url="/login/")
def home_view(request):
    latest_products = Product.objects.exclude(updated_at__isnull=True).order_by(
        "-updated_at"
    )[
        :5
    ]  # 获取最后编辑时间最近的5个产品
    latest_flowers = FlowerMaterial.objects.exclude(updated_at__isnull=True).order_by(
        "-updated_at"
    )[
        :5
    ]  # 获取最后编辑时间最近的5个花材
    return render(
        request,
        "home.html",
        {
            "latest_products": latest_products,
            "latest_flowers": latest_flowers,
        },
    )


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UserUpdateForm, CustomPasswordChangeForm


@login_required
def profile_view(request):
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        password_form = CustomPasswordChangeForm(request.user, request.POST)

        if "update_profile" in request.POST:
            if user_form.is_valid():
                user_form.save()
                messages.success(request, "您的个人资料已成功更新！")
                return redirect("profile")
        elif "change_password" in request.POST:
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # 重要！
                messages.success(request, "您的密码已成功更新！")
                return redirect("profile")

    else:
        user_form = UserUpdateForm(instance=request.user)
        password_form = CustomPasswordChangeForm(request.user)

    context = {
        "user_form": user_form,
        "password_form": password_form,
        "current_user": request.user,
    }
    return render(request, "profile.html", context)


#############################用户############################


def base_view(request):
    return render(request, "base.html", {"current_user": request.user})


def login_view(request):
    return render(request, "login.html", {"current_user": request.user})


def logout_view(request):
    logout(request)
    return redirect("home", {"current_user": request.user})


def success_page(request):
    return render(request, "success.html")


def control_panel_view(request):
    return render(request, "control_panel.html", {"current_user": request.user})


def QuoteMOD_view(request):
    return render(request, "QuoteMOD.html", {"current_user": request.user})


def success_page(request):
    return render(request, "success.html")


##########################普通视图END##############################


###############################报价单##############################
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import Product, Quote, QuoteItem
import json
from decimal import Decimal


def add_quote_item(request):
    products = Product.objects.all()
    return render(request, "add_quote_item.html", {"products": products})


@csrf_exempt
def save_quote(request):
    if request.method == "POST":
        data = json.loads(request.body)
        products = data["products"]
        total_amount = Decimal(data["totalAmount"])
        grand_total = Decimal(data["grandTotal"])
        freight_cost = Decimal(data["freightCost"])
        shipper = data["shipper"]
        buyer = data["buyer"]
        receiver = data["receiver"]
        tel = data["tel"]
        invoice_no = data["invoiceNo"]
        payment_term = data["paymentTerm"]
        deliver_time = data["deliverTime"]
        payment_currency = data["paymentCurrency"]
        beneficiary_account_number = data["beneficiaryAccountNumber"]
        swift_code = data["swiftCode"]
        beneficiary_country = data["beneficiaryCountry"]
        beneficiary_name = data["beneficiaryName"]
        beneficiary_address = data["beneficiaryAddress"]
        beneficiary_bank = data["beneficiaryBank"]
        beneficiary_bank_address = data["beneficiaryBankAddress"]
        bank_code = data["bankCode"]
        branch_code = data["branchCode"]
        remark = data["remark"]

        # Create Quote instance
        quote = Quote(
            shipper=shipper,
            buyer=buyer,
            receiver=receiver,
            tel=tel,
            invoice_no=invoice_no,
            valid_date=timezone.now() + timezone.timedelta(days=30),
            freight_cost=freight_cost,
            total=total_amount,
            grand_total=grand_total,
            payment_term=payment_term,
            deliver_time=deliver_time,
            payment_currency=payment_currency,
            beneficiary_account_number=beneficiary_account_number,
            swift_code=swift_code,
            beneficiary_country=beneficiary_country,
            beneficiary_name=beneficiary_name,
            beneficiary_address=beneficiary_address,
            beneficiary_bank=beneficiary_bank,
            beneficiary_bank_address=beneficiary_bank_address,
            bank_code=bank_code,
            branch_code=branch_code,
            remark=remark,
            created_by=request.user,
        )
        quote.save()

        # Create QuoteItem instances
        for product in products:
            model = product["model"]
            picture = product["picture"]
            specification = product["specification"]
            color = product["color"]
            qty = int(product["qty"])
            cost_price = Decimal(product["costPrice"])
            unit_price = Decimal(product["unitPrice"])
            amount = Decimal(product["amount"])
            profit_margin = Decimal(product["profitMargin"])

            quote_item = QuoteItem(
                quote=quote,
                model=model,
                picture=picture,
                specification=specification,
                color=color,
                qty=qty,
                cost_price=cost_price,
                unit_price=unit_price,
                amount=amount,
                profit_margin=profit_margin,
            )
            quote_item.save()

        return JsonResponse({"status": "success", "quote_id": quote.id})
    return JsonResponse(
        {"status": "error", "message": "Invalid request method"}, status=400
    )


###############################报价单end############################

#########################注册登录############################
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


# 登录
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


#########################注册登录END############################
##########################花材###############################

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import FlowerMaterialForm
from .models import Category, Supplier, Process, Grade


@login_required
def add_flower_material(request):
    if request.method == "POST":
        form = FlowerMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            flower_material = form.save(commit=False)
            flower_material.created_by = request.user  # 将创建者设置为当前用户
            flower_material.save()
            return redirect("flower_material_list")  # 替换为你的重定向URL
    else:
        form = FlowerMaterialForm()

    categories = Category.objects.all()
    suppliers = Supplier.objects.all()
    processes = Process.objects.all()
    grades = Grade.objects.all()

    return render(
        request,
        "add_flower_material.html",
        {
            "form": form,
            "categories": categories,
            "suppliers": suppliers,
            "processes": processes,
            "grades": grades,
            "created_by": request.user,
            "current_user": request.user,
        },
    )


# 花材表显示
def flower_materials_list(request):
    flower_materials = FlowerMaterial.objects.all()
    return render(
        request,
        "flower_material_list.html",
        {"flower_materials": flower_materials, "current_user": request.user},
    )


# 花材详情页
def flower_material_detail(request, model):
    material = get_object_or_404(FlowerMaterial, model=model)
    flower_materials = FlowerMaterial.objects.all()
    return render(
        request,
        "flower_material_detail.html",
        {
            "material": material,
            "flower_materials": flower_materials,
            "current_user": request.user,
        },
    )


# 花材编辑
def edit_flower_material(request, model):
    material = get_object_or_404(FlowerMaterial, model=model)
    if request.method == "POST":
        form = FlowerMaterialForm(request.POST, request.FILES, instance=material)
        if form.is_valid():
            flower_material = form.save(commit=False)
            flower_material.created_by = request.user
            flower_material.save()
            return redirect("flower_material_detail", model=material.model)
    else:
        form = FlowerMaterialForm(instance=material)

    categories = Category.objects.all()
    colors = Color.objects.all()
    processes = Process.objects.all()
    suppliers = Supplier.objects.all()
    grades = Grade.objects.all()
    flower_materials = FlowerMaterial.objects.all()

    context = {
        "form": form,
        "material": material,
        "categories": categories,
        "colors": colors,
        "processes": processes,
        "suppliers": suppliers,
        "grades": grades,
        "flower_materials": flower_materials,
        "current_user": request.user,
    }

    return render(request, "flower_material_edit.html", context)


# 花材删除
from django.shortcuts import get_object_or_404, redirect, render


def delete_flower_material(request, model):
    material = get_object_or_404(FlowerMaterial, model=model)
    if request.method == "POST":
        material.delete()
        return redirect("flower_material_list")  # 重定向到花材列表页
    return render(
        request, "flower_material_confirm_delete.html", {"material": material}
    )


##########################花材end###############################


###############################产品####################################
from django.db import transaction, IntegrityError
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.forms import modelform_factory
from .models import Product, FlowerMaterial, ProductMaterial
from django.contrib.auth.decorators import login_required
from django.utils import timezone


from django.shortcuts import render, redirect
from django.forms import modelform_factory
from django.utils import timezone
from django.db import transaction, IntegrityError
from .models import Product, FlowerMaterial, ProductMaterial


@login_required
def add_product(request):
    # 使用 modelform_factory 创建 Product 表单，不包含 'materials', 'created_by', 'created_at', 'updated_at'
    ProductForm = modelform_factory(
        Product, exclude=["materials", "created_by", "created_at", "updated_at"]
    )

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)  # 添加 request.FILES
        if form.is_valid():
            try:
                with transaction.atomic():
                    product = form.save(commit=False)
                    product.created_by = request.user
                    product.created_at = timezone.now()
                    product.updated_at = timezone.now()
                    product.save()

                    # 处理花材信息
                    flower_materials = request.POST.get("flower_materials", "").split(
                        ";"
                    )
                    for fm in flower_materials:
                        if fm:  # 检查 fm 是否为空字符串
                            flower_material_model, quantity, ratio, cost_price = (
                                fm.split(",")
                            )
                            flower_material = FlowerMaterial.objects.get(
                                model=flower_material_model
                            )
                            ProductMaterial.objects.create(
                                product=product,
                                flower_material=flower_material,
                                quantity=quantity,
                                ratio=ratio,
                            )

                    return redirect("product_list")  # 重定向到一个成功页面
            except IntegrityError:
                form.add_error(None, "保存产品时出现错误，请重试。")
            except FlowerMaterial.DoesNotExist:
                form.add_error(None, "指定的花材不存在，请检查输入。")
    else:
        form = ProductForm()
        flower_materials = FlowerMaterial.objects.all()

    return render(
        request,
        "add_product.html",
        {
            "form": form,
            "flower_materials": flower_materials,
            "current_user": request.user,
        },
    )


from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory
from django.db import transaction, IntegrityError
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from .models import Product, FlowerMaterial, ProductMaterial


@login_required
def edit_product(request, model):
    ProductForm = modelform_factory(
        Product, exclude=["materials", "created_by", "created_at", "updated_at"]
    )

    product = get_object_or_404(Product, model=model)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            try:
                with transaction.atomic():
                    product = form.save(commit=False)
                    product.created_by = request.user
                    product.updated_at = timezone.now()
                    product.save()

                    # 处理花材信息
                    ProductMaterial.objects.filter(product=product).delete()
                    flower_materials = request.POST.get("flower_materials", "").split(
                        ";"
                    )
                    for fm in flower_materials:
                        if fm:
                            flower_material_model, quantity, ratio, cost_price = (
                                fm.split(",")
                            )
                            flower_material = FlowerMaterial.objects.get(
                                model=flower_material_model
                            )
                            ProductMaterial.objects.create(
                                product=product,
                                flower_material=flower_material,
                                quantity=quantity,
                                ratio=ratio,
                            )

                    return redirect("product_list")  # 重定向到产品列表页面
            except IntegrityError:
                form.add_error(None, "保存产品时出现错误，请重试。")
            except FlowerMaterial.DoesNotExist:
                form.add_error(None, "指定的花材不存在，请检查输入。")
    else:
        form = ProductForm(instance=product)
        flower_materials = FlowerMaterial.objects.all()

        # 获取现有的花材信息，用于前端展示
        existing_materials = ProductMaterial.objects.filter(product=product)

    return render(
        request,
        "edit_product.html",
        {
            "form": form,
            "flower_materials": flower_materials,
            "existing_materials": existing_materials,
            "current_user": request.user,
        },
    )


def delete_product(request, model):
    product = get_object_or_404(Product, model=model)
    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    return render(request, "delete_product.html", {"product": product})


from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(
        request,
        "product_list.html",
        {
            "products": products,
            "current_user": request.user,
        },
    )


def product_details(request, model):
    product = get_object_or_404(Product, model=model)
    materials = product.productmaterial_set.all()

    context = {
        "product": product,
        "materials": materials,
        "current_user": request.user,
    }
    return render(request, "product_details.html", context)


##########################产品END#######################


##############################客户###############################
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import CustomerForm


@login_required
def customer_list(request):
    if request.user.is_superuser:
        customers = Customer.objects.all()
    else:
        customers = Customer.objects.filter(created_by=request.user)
    return render(
        request,
        "customer_list.html",
        {"customers": customers, "current_user": request.user},
    )


from .models import Customer
from .forms import CustomerForm


@login_required
def add_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created_by = request.user
            customer.save()
            return redirect("customer_list")
    else:
        form = CustomerForm()
    return render(
        request, "add_customer.html", {"form": form, "current_user": request.user}
    )


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Customer, FollowUpRecord
from .forms import FollowUpRecordForm


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Customer, FollowUpRecord
from .forms import FollowUpRecordForm
from .models import Customer, FollowUpRecord, FollowUpAttachment
from .forms import FollowUpRecordForm, FollowUpAttachmentForm


# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Customer, FollowUpRecord, FollowUpAttachment
from .forms import FollowUpRecordForm, FollowUpAttachmentForm


@login_required
def follow_up_list(request, customer_id):
    customer = get_object_or_404(Customer, customer_id=customer_id)
    follow_ups = customer.follow_ups.all().order_by("-follow_up_time")

    # Add logic to determine if attachment is an image
    for follow_up in follow_ups:
        for attachment in follow_up.attachments.all():
            attachment.is_image = attachment.file.url.lower().endswith(
                (".png", ".jpg", ".jpeg")
            )

    if request.method == "POST":
        form = FollowUpRecordForm(request.POST)
        files = request.FILES.getlist("file")
        if form.is_valid():
            follow_up = form.save(commit=False)
            follow_up.customer = customer
            follow_up.created_by = request.user
            follow_up.follow_up_count = follow_ups.count() + 1
            follow_up.save()
            for file in files:
                FollowUpAttachment.objects.create(follow_up_record=follow_up, file=file)
            return redirect("follow_up_list", customer_id=customer_id)
    else:
        form = FollowUpRecordForm()
        attachment_form = FollowUpAttachmentForm()
    return render(
        request,
        "follow_up_list.html",
        {
            "customer": customer,
            "follow_ups": follow_ups,
            "form": form,
            "attachment_form": attachment_form,
            "current_user": request.user,
        },
    )
