from django.urls import path
from todo_app import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('create/', views.create_todo, name='create_todo'),
    path('update/<int:id>/', views.update_view, name="update_todo"),
    path('delete/<int:id>/', views.delete_view, name="delete_todo"),
    path('show/<id>/', views.show_view, name="show_todo")

    # path('data/', my_view, name="my_view"),
    # path('nicat/', view_picture, name="view_picture"),
    # path("nicat_test/", new_test ),

]
