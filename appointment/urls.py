from django.urls import path
from . import views

urlpatterns = [
    path(
        '<int:pk>/my_appointments/',
        views.MyAppointmentsList.as_view(),
        name='my_appointments'),
    path(
        '<int:pk>/book/',
        views.MakeAppointment.as_view(),
        name='book'),
    path(
        '<int:pk>/edit_appointment/',
        views.EditAppointment.as_view(),
        name='edit_appointment'),
    path(
        '<int:pk>/cancel/',
        views.DeleteAppointment.as_view(),
        name='cancel'),
]
