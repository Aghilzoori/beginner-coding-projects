from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),  # صفحه داشبورد
    path('api/register/', views.register_user, name='api_register'),
    path('api/check_login/', views.check_login, name='api_check_login'),
]