from django.urls import path
from .views import dashboard, add_data, update_view

urlpatterns = [

    path('', dashboard, name="dashboard"),
    path('product/<int:id>/update', update_view, name="update_view"),
    path('test/', add_data, name="add_data"),

]
