from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from .models import Customer


class UpdateProfileForm(forms.ModelForm):
    """
    Update custom profile details linked to Customer model
    """
    class Meta:
        model = Customer
        fields = (
            'profile_pic',
            'date_of_wedding',
            'partners_name',
            'wedding_location',
            'wedding_theme',
            'website_url')
        widgets = {
            'profile_pic': forms.FileInput(
                attrs={'class': 'form-control', 'type': 'file'}),
            'date_of_wedding': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'partners_name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'wedding_location': forms.TextInput(
                attrs={'class': 'form-control'}),
            'wedding_theme': forms.TextInput(
                attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(
                attrs={'class': 'form-control'}),
        }


class CreateNewProfileForm(forms.ModelForm):
    """
    Create custom profile linked to Customer model
    """
    class Meta:
        model = Customer
        fields = (
            'profile_pic',
            'date_of_wedding',
            'partners_name',
            'wedding_location',
            'wedding_theme',
            'website_url')
        widgets = {
            'profile_pic': forms.FileInput(
                attrs={'class': 'form-control', 'type': 'file'}),
            'date_of_wedding': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}),
            'partners_name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'wedding_location': forms.TextInput(
                attrs={'class': 'form-control'}),
            'wedding_theme': forms.TextInput(
                attrs={'class': 'form-control'}),
            'website_url': forms.TextInput(
                attrs={'class': 'form-control'}),
        }


class EditAccountSettingsForm(UserChangeForm):
    """
    Form to edit account details on User model
    """
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class UpdatePasswordForm(PasswordChangeForm):
    """
    Update password form
    """
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'type': 'password'}))

    class Meta:
        model = User
        fields = ('old_password', 'new_password1', 'new_password2')


class RegistrationForm(UserCreationForm):
    """
    Custom registration form
    """
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}))
    first_name = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))
    last_name = forms.CharField(
        max_length=100, widget=forms.TextInput(
            attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2')

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
