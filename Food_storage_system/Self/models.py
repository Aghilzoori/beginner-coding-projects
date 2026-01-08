from django.db import models

class Student(models.Model):
    full_name = models.CharField(max_length=200, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    national_code = models.IntegerField(null=True, blank=True)
    ID_number = models.IntegerField(null=True, blank=True)
    Inventory = models.IntegerField(null=True, blank=True)
# Create your models here.

class DailyFood(models.Model):
    DAY_CHOICES = [
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
    ]

    day = models.CharField(max_length=3, choices=DAY_CHOICES, unique=True)

    breakfast = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='صبحانه'
    )
    lunch = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='ناهار'
    )
    dinner = models.CharField(
        max_length=200, blank=True, null=True, verbose_name='شام'
    )

    total_price = models.IntegerField(
        blank=True, null=True, verbose_name='قیمت کل روز'
    )

    def __str__(self):
        return dict(self.DAY_CHOICES).get(self.day, self.day)
