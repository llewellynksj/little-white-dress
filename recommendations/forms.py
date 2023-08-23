from django.contrib.auth.models import User
from django import forms
from .models import Recommendation


class AddNewRecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = ('type_of_recommendation', 'title', 'location', 'link', 'summary', 'posted_by',)
        widgets = {
            'type_of_recommendation': forms.Select(attrs={'class': 'form-control', 'type': 'select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control', 'type': 'url'}),
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            # 'date_posted': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'posted_by': forms.TextInput(attrs={'class': 'form-control'}),
        }
