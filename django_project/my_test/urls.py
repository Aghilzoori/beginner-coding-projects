from django.urls import path
from . import views

urlpatterns = [
    path('', views.friend_list, name='friend_list'),
    path('add/', views.add_friend, name='add_friend'),
    path('delete/<int:friend_id>/', views.delete_friend_page, name='delete_friend_page'),
    path('delete-confirm/<int:friend_id>/', views.delete_friend, name='delete_friend'),
    path('profile/add/<int:friend_id>/', views.add_profile, name='add_profile'),
    path('profile/delete/<int:friend_id>/', views.delete_profile, name='delete_profile'),
]
