from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from Self.models import Student, DailyFood
from .models import Reservation

# ============ 1. لاگین ============
def login_view(request):
    """صفحه لاگین - اولین صفحه سایت"""
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        national_code = request.POST.get("national_code")
        ID_number = request.POST.get("ID_number")

        try:
            student = Student.objects.get(
                full_name=full_name,
                national_code=national_code,
                ID_number=ID_number
            )
            request.session['student_id'] = student.id
            request.session['student_name'] = student.full_name
            request.session['student_inventory'] = student.Inventory or 0
            
            return redirect('ho')
            
        except Student.DoesNotExist:
            error = "اطلاعات وارد شده اشتباه است!"
            return render(request, "login.html", {"error": error})
    
    return render(request, "login.html")


# ============ 2. صفحه اصلی ============
def ho(request):
    """صفحه اصلی کاربر بعد از لاگین"""
    if 'student_id' not in request.session:
        messages.error(request, "لطفاً ابتدا وارد شوید")
        return redirect('login')
    
    student_id = request.session['student_id']
    student = get_object_or_404(Student, id=student_id)
    
    user_reservations = Reservation.objects.filter(student=student)
    
    from datetime import datetime
    import calendar
    
    today = datetime.now()
    today_name = calendar.day_name[today.weekday()].lower()[:3]  
    
    day_mapping = {
        'mon': 'mon', 'tue': 'tue', 'wed': 'wed',
        'thu': 'thu', 'fri': 'fri', 'sat': 'sat', 'sun': 'sun'
    }
    
    today_code = day_mapping.get(today_name, 'mon')
    
    try:
        today_food = DailyFood.objects.get(day=today_code)
    except DailyFood.DoesNotExist:
        today_food = None
    
    all_foods = DailyFood.objects.all()
    
    context = {
        'student': student,
        'today_food': today_food,
        'foods': all_foods,
        'reservations': user_reservations,
        'today_name': today_code,
    }
    
    return render(request, "h.html", context)


# ============ 3. رزرو غذا ============
def reservation(request, student_id):
    student = get_object_or_404(Student, id=student_id)

   
    DAY_CHOICES = [
        ('sat', 'شنبه'),
        ('sun', 'یکشنبه'),
        ('mon', 'دوشنبه'),
        ('tue', 'سه‌شنبه'),
        ('wed', 'چهارشنبه'),
        ('thu', 'پنجشنبه'),
        ('fri', 'جمعه'),
    ]

    error = None  

    if request.method == "POST":
        day = request.POST.get('day')

        try:
            daily_food = DailyFood.objects.get(day=day)
            price = daily_food.total_price if daily_food.total_price else 0

            if student.Inventory >= price:
                student = get_object_or_404(Student, id=student_id)
                has_reservation = Reservation.objects.filter(
                    student=student,
                    day=str(day)  
                ).exists()
                if has_reservation:
                    error = "شما قبلا رزرو کردین"
                else:
                    student.Inventory -= price
                    student.save()

                    reservation = Reservation.objects.create(
                        student=student,
                        daily_food=daily_food,
                        day=day,
                        price=price
                    )

                    request.session['student_inventory'] = student.Inventory

                    return redirect('ho')
            else:
                error = "موجودی کافی نیست!"
        except DailyFood.DoesNotExist:
            error = "برای این روز غذایی تعریف نشده است!"

    return render(request, 'reservation.html', {
        'student': student,
        'day_choices': DAY_CHOICES,
        'error': error
    })

def list_food(request):
    food = Reservation.objects.all()
    return render(request, "h.html", {"food":food})
def delete_food(request):
    if 'student_id' not in request.session:
        return redirect('login')

    student_id = request.session['student_id']
    Reservation.objects.filter(student_id=student_id).delete()

    return redirect('ho')
