from django.db import models
from django.contrib.auth.models import User
import datetime


class Appointment(models.Model):
    TIME_SLOTS = [
        ('09:00', '09:00'),
        ('11:30', '11:30'),
        ('14:00', '14:00'),
        ('16:30', '16:30'),
    ]

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE
    )
    date = models.DateField(
        default=datetime.date.today
    )
    time = models.CharField(
        max_length=20,
        choices=TIME_SLOTS
    )
    date_of_wedding = models.DateField(
        default=datetime.date.today
    )
    no_in_party = models.PositiveSmallIntegerField(
        help_text='Please note max number of guests is 5 (not including yourself)'
    )

    def __str__(self):
        return f"Appointment: {self.date} {self.time} - {self.user.first_name} {self.user.last_name}"
