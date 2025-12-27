# users/models.py
from django.db import models

class UserProfile(models.Model):
    username = models.CharField(
        max_length=100, 
        unique=True, 
        verbose_name="نام کاربری"
    )
    fullname = models.CharField(max_length=200, verbose_name="نام و نام خانوادگی")
    province = models.CharField(max_length=100, verbose_name="استان")
    city = models.CharField(max_length=100, verbose_name="شهر")
    school = models.CharField(max_length=200, verbose_name="مدرسه")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    
    class Meta:
        verbose_name = "پروفایل کاربر"
        verbose_name_plural = "پروفایل کاربران"
    
    def __str__(self):
        return f"{self.fullname} ({self.username})"