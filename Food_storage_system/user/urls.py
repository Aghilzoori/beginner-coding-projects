from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.ho, name='ho'),
    path('reservation/<int:student_id>/', views.reservation, name='reservation'),
    path('home/', views.list_food, name="list_food"),
    path('delete-food/', views.delete_food, name='delete_food'),

]