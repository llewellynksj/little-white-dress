from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Appointment
from .forms import MakeBookingForm


class DeleteAppointment(generic.DeleteView):
    """
    Delete Appointment
    """
    model = Appointment
    template_name = 'cancel.html'

    def get_success_url(self) -> str:
        return reverse_lazy(
            'my_appointments', kwargs={'pk': self.object.pk}
        )


class EditAppointment(generic.UpdateView):
    """
    Displays form for user to update thier current booking
    """
    model = Appointment
    form_class = MakeBookingForm
    template_name = 'edit_appointment.html'

    def get_success_url(self) -> str:
        return reverse_lazy(
            'my_appointments', kwargs={'pk': self.object.pk}
        )


class MakeAppointment(generic.CreateView):
    """
    Links to custom booking form
    """
    model = Appointment
    form_class = MakeBookingForm
    template_name = 'book.html'

    # Make the user id available to be able to be saved to the form
    # Code from Codemy 'Profile Account Creation - Django Blog #32' video:
    # https://bit.ly/44Ymcjg
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy(
            'my_appointments', kwargs={'pk': self.object.pk}
        )


class MyAppointmentsList(generic.ListView):
    """
    Displays all appointments currently held by User
    """
    model = Appointment
    template_name = 'my_appointments.html'

    # code adapted from Codemy 'Create a Blog Profile Page' Video:
    # http://bit.ly/3OsUgy8:
    def get_context_data(self, *args, **kwargs):
        context = super(
            MyAppointmentsList, self).get_context_data(
                *args, **kwargs)
        user_appointments = Appointment.objects.filter(
            user=self.request.user
        )
        context['user_appointments'] = user_appointments
        return context
