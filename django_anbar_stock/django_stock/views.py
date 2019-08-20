from django.shortcuts import render, redirect
from .forms import ProductForm
from django.http import HttpResponse
from faker import Faker
from .models import Company, Product
from django.contrib import messages
from datetime import datetime


# Create your views here.


def dashboard(request):
    context = {}
    context["form"] = ProductForm()
    context["company_list"] = Company.objects.all()
    context["product_list"] = Product.objects.all()
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            messages.success(
                request, f"{product.name} ugurla elave edildi"
            )
            return redirect("dashboard")
        else:
            context["form"] = form
    return render(request, "dashboard.html", context)


def update_view(request, id):
    context = {}
    product = Product.objects.filter(id=id).last()
    if product:
        context["product"] = Product.objects.filter(id=id).last()
        context["form"] = ProductForm(
            instance=product
        )
        return render(request, "includes/product_form.html", context)
    else:
        return redirect("dashboard")


def add_data(request):
    fake = Faker()
    for x in range(100):
        Company.objects.create(
            name=fake.company()
        )
    return HttpResponse("Success")
