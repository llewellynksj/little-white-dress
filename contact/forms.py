from django import forms
from django.forms import ModelForm
from .models import Enquiry


class EnquiryForm(ModelForm):
    """
    Contact Form links with Enquiry model
    """
    class Meta:
        model = Enquiry
        fields = ('full_name', 'email', 'message')
        widgets = {
            'full_name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control'}),
            'message': forms.Textarea(
                attrs={'class': 'form-control', 'cols': '80', 'rows': '10'}),
        }
