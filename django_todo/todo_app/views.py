from django.shortcuts import render, redirect
from .forms import TodoForm, TodoModel
from django.http import HttpResponse


# Create your views here.

def home_page(request):
    context = {}
    context["todo_list"] = TodoModel.objects.all()
    return render(request, "todo.html", context)


def create_todo(request):
    if request.method == "POST":
        data = request.POST
        form = TodoForm(data)
        if form.is_valid():  # eger form duzgundurse
            form.save()
            return redirect("home")
        else:  # eger form yanlishdirsa
            context = {}
            context["form"] = form
            return render(request, "todo_form.html", context)
    else:
        context = {}
        context["form"] = TodoForm()
        return render(request, "todo_form.html", context)


def update_view(request, id):
    todo = TodoModel.objects.filter(id=id).last()
    if request.method == "GET":
        if todo:
            form = TodoForm(instance=todo)
            context = {}
            context["form"] = form
            return render(request, "todo_form.html", context)
        else:
            return HttpResponse("Bele bir obyekt yoxdur!")
    else:
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            context = {}
            context["form"] = form
            return render(request, "todo_form.html", context)


def delete_view(request, id):
    todo = TodoModel.objects.filter(id=id).last()
    if request.method == "GET":
        context = {}
        context["todo"] = todo
        return render(request, "delete_todo.html", context)
    else:
        todo.delete()
        return redirect("home")

def show_view(request, id):
    todo = TodoModel.objects.filter(id=id).last()
        context = {}
        context["todo"] = todo
        return render(request, "show_todo_details.html", context)



# def my_view(request):
#     data = {'name': 'nicat', 'arr': []}
#     for i in range(100):
#         data['arr'].append(i)
#     return render(request, "my_view.html", data)
#
# #
# def view_picture(request):
#     data = {
#         'url': 'https://images.unsplash.com/photo-1518796745738-41048802f99a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80'}
#     return render(request, "view_picture.html", data)
#
# def view_picture_2(request):
#     data = {}
#     data["url"] = 'https://images.unsplash.com/photo-1518796745738-41048802f99a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&w=1000&q=80'
#     return render(request, "view_picture.html", data)
#
#
# def new_test(request):
#     context = {}
#     context["hello"] = {
#         "my_key": "this_value"
#     }
#     return render(request,'view_picture.html', context)
