from django.contrib.auth.models import User
from django import forms
from .models import Appointment


class MakeBookingForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = (
            'date',
            'time',
            'date_of_wedding',
            'no_in_party',
        )
        widgets = {
            'date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.Select(
                attrs={'class': 'form-control', 'type': 'select'}),
            'date_of_wedding': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'no_in_party': forms.TextInput(
                attrs={'class': 'form-control'}),
        }
