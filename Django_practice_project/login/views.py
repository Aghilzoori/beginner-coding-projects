# در login/views.py
from django.shortcuts import render
from django.http import HttpResponse
    
# یا برای صفحه‌ای با تمپلیت:
def login_view(request):
    return render(request, '/home/aghil/Desktop/django_test_1/login/templates/login.html') 