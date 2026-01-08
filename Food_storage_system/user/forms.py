from django import forms
from .models import Reservation, DailyFood

DAY_CHOICES = DailyFood.DAY_CHOICES

class MultiDayReservationForm(forms.Form):
    days = forms.MultipleChoiceField(
        choices=DAY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label="روزهای هفته"
    )
    breakfast = forms.BooleanField(required=False, label="صبحانه")
    lunch = forms.BooleanField(required=False, label="ناهار")
    dinner = forms.BooleanField(required=False, label="شام")
