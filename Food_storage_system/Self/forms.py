from django import forms
from .models import Student, DailyFood

class StudentForms(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["full_name", 'number', 'national_code', 'ID_number', 'Inventory']
        
class DailyFoodForms(forms.ModelForm):
    class Meta:
        model = DailyFood
        fields = ['day', 'breakfast', 'lunch', 'dinner', 'total_price']