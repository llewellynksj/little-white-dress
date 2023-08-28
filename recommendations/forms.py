from django.contrib.auth.models import User
from django import forms
from .models import Recommendation


class AddNewRecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = (
            'type_of_recommendation',
            'title',
            'location',
            'web_link',
            'summary',
            'posted_by',
            'decleration_of_consent',
        )
        widgets = {
            'type_of_recommendation': forms.Select(
                attrs={'class': 'form-control', 'type': 'select'}),
            'title': forms.TextInput(
                attrs={'class': 'form-control'}),
            'location': forms.TextInput(
                attrs={'class': 'form-control'}),
            'web_link': forms.TextInput(
                attrs={'class': 'form-control'}),
            'summary': forms.TextInput(
                attrs={'class': 'form-control'}),
            'posted_by': forms.TextInput(
                attrs={'class': 'form-control'}),
            'decleration_of_consent': forms.CheckboxInput(
                attrs={'class': 'form-check', 'required': 'True'}),
        }
