from django.db import models
from Self.models import Student, DailyFood

class Reservation(models.Model):
    """مدل رزرو غذا"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    daily_food = models.ForeignKey(DailyFood, on_delete=models.CASCADE)
    
    
    day = models.CharField(max_length=10, default='sun')  
    price = models.IntegerField(default=0)  
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.student.full_name} - {self.day}"