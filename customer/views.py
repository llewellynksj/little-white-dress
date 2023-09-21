from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import RegistrationForm, UpdatePasswordForm
from .forms import EditAccountSettingsForm, CreateNewProfileForm
from .forms import UpdateProfileForm
from django.contrib.auth.models import User
from .models import Customer
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver
from django.contrib import messages


@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    """
    Displays successfully logged out message when user logs out
    """
    messages.add_message(
        request, messages.INFO, 'You have successfully logged out')


class UpdateCustomerProfile(SuccessMessageMixin, generic.UpdateView):
    """
    Displays update profile page
    """
    model = Customer
    template_name = 'update_profile.html'
    form_class = UpdateProfileForm
    success_message = 'Your profile was updated successfully'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # Direct user to their Profile page when form submitted
    def get_success_url(self) -> str:
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})


class CustomerProfile(generic.ListView):
    """
    Displays customer profile page
    """
    model = Customer
    template_name = 'profile.html'

    # code from Codemy 'Create a Blog Profile Page' Video:
    # http://bit.ly/3OsUgy8:
    def get_context_data(self, *args, **kwargs):
        context = super(
            CustomerProfile, self).get_context_data(
                *args, **kwargs)
        customer_profile = get_object_or_404(Customer, id=self.kwargs['pk'])
        context['customer_profile'] = customer_profile
        return context


class CreateNewProfile(SuccessMessageMixin, generic.CreateView):
    """
    Links to custom profile form
    """
    model = Customer
    form_class = CreateNewProfileForm
    template_name = 'create_profile.html'
    success_message = 'Your profile has been created successfully'

    # Make the user id available to be able to be saved to the form
    # Code from Codemy 'Profile Account Creation - Django Blog #32' video:
    # https://bit.ly/44Ymcjg
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})


class AccountSettings(SuccessMessageMixin, generic.UpdateView):
    """
    Links to custom account settings form
    """
    form_class = EditAccountSettingsForm
    template_name = 'registration/account_settings.html'
    success_message = 'Your account settings have been updated successfully'

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # Direct user to their Profile page when form submitted
    def get_success_url(self) -> str:
        return reverse_lazy('profile', kwargs={'pk': self.object.pk})


class UpdatePassword(SuccessMessageMixin, PasswordChangeView):
    """
    Links to custom password form
    """
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('settings')
    success_message = 'Your password has been updated successfully'


class CustomerRegistration(SuccessMessageMixin, generic.CreateView):
    """
    Links custom registration form to registration template
    """
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('login')
    success_message = 'Your registration was successful'
