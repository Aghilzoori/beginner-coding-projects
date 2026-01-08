from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, DailyFood
from .forms import StudentForms, DailyFoodForms
from django.views.decorators.http import require_POST
from user.models import Reservation
from datetime import datetime
from functools import wraps
from django.http import HttpResponse

def home(request):
    food = DailyFood.objects.all()
    friends = Student.objects.all()
    return render(request, "my_test/home.html", {"food": food, "friends": friends})


def student_list(request):
    studens = Student.objects.all()  
    return render(request, 'my_test/home.html', {'friends': studens})

def add_student(request):
    if request.method == 'POST':
        form = StudentForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForms()

    return render(request, 'my_test/add_student.html', {'form': form})

def delete_student(request, friend_id):
    if request.method == 'POST':
        student = Student.objects.get(id=friend_id)
        student.delete()
    return redirect('home')

def add_Inventory(request, friend_id):
    student = get_object_or_404(Student, id=friend_id)
    if request.method == 'POST':
        Inventory_url = request.POST.get('Inventory')
        student.Inventory = Inventory_url
        student.save()
        return redirect('home')
    return render(request, 'my_test/add_Inventory.html', {'friend': student})


def delete_Inventory(request, friend_id):
    if request.method == 'POST':
        student = get_object_or_404(Student, id=friend_id)
        student.Inventory = None
        student.save()
    return redirect('home')

def Add_food(request):
    if request.method == "POST":
        form = DailyFoodForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = DailyFoodForms()

    return render(request, "my_test/add_food.html", {"form": form})

def list_food(request):
    food = DailyFood.objects.all()
    return render(request, "my_test/home.html", {"food":food})
def list_student(request):
    reservations = Reservation.objects.select_related(
        'student', 'daily_food'
    ).all()

    return render(request, "my_test/home.html", {
        "reservations": reservations,
    })

@require_POST
def delete_food(request):
    """حذف همه غذاها"""
    DailyFood.objects.all().delete()
    return redirect('home')
# Create your views here.


def only_friday(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if datetime.today().weekday() == 4:  
            return func(*args, **kwargs)
        return HttpResponse(status=204)  
    return wrapper

@only_friday
def delete_foods(request):
    DailyFood.objects.all().delete()
    return HttpResponse(status=204)
