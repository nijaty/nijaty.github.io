from django.shortcuts import render
from .models import Footer, Copyright, Common, Menu


# Create your views here.


def index(request):
    context = {}
    context["footer_list"] = Footer.objects.all()
    context["copyright"] = Copyright.objects.all()[0].title
    context["title_list"] = Common.objects.all()
    context["logo_title"] = Common.objects.all()[0].logo_title
    # context["about_title"] = Common.objects.all()[3].logo_title
    context["menu_list"] = Menu.objects.all()
    return render(request, "index.html", context)
