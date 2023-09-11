from django.shortcuts import render


def DisplayAppointment(request):
    return render(request, 'appointment.html', {})
