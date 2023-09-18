from django.contrib import admin
from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_filter = ('booking_date',)
    search_fields = ['booking_date', 'user']
