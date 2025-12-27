from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path('', views.login_view, name='login'),
]