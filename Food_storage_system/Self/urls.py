from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  
    path('add/', views.add_student, name='add_student'),
    path('delete/<int:friend_id>/', views.delete_student, name='delete_student'),
    path('inventory/add/<int:friend_id>/', views.add_Inventory, name='add_Inventory'),
    path('inventory/delete/<int:friend_id>/', views.delete_Inventory, name='delete_inventory'),
    path('add-food/', views.Add_food, name='add_food'),
    path('inventory/delete_food/', views.delete_food, name="delete_food"),
    path('list_student/', views.list_student, name="list_student"),

]




