from django.shortcuts import render
from .models import Menu


# Create your views here.


def index_view(request):
    context = {}
    context["menu_list"] = Menu.objects.all()
    return render(request, 'index.html', context)
