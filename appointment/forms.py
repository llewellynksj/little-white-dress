from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import datetime
from datetime import datetime
from django import forms
from .models import Appointment


class MakeBookingForm(forms.ModelForm):
    """
    Booking Form to get booking information
    for appointment model from user
    """
    class Meta:
        model = Appointment
        fields = (
            'booking_date',
            'time',
            'date_of_wedding',
            'no_in_party',
        )
        widgets = {
            'booking_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.Select(
                attrs={'class': 'form-control', 'type': 'select'}),
            'date_of_wedding': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'no_in_party': forms.TextInput(
                attrs={'class': 'form-control'}),
        }
