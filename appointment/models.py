from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from datetime import datetime


class Appointment(models.Model):
    TIME_SLOTS = [
        ('09:00', '09:00'),
        ('11:30', '11:30'),
        ('14:00', '14:00'),
        ('16:30', '16:30'),
    ]

    def validate_weekday(booking_date):
        if not booking_date == datetime.weekday:
            raise ValidationError(
                "LWD is not open at the weekend. Please choose another day")

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE
    )
    booking_date = models.DateField(
        default=datetime.today,
        validators=[validate_weekday]
    )
    time = models.CharField(
        max_length=20,
        choices=TIME_SLOTS,
        help_text='All appointments are allocated 2 hours'
    )
    date_of_wedding = models.DateField(
        default=datetime.today
    )
    no_in_party = models.PositiveSmallIntegerField(
        help_text='Please note max number of additional guests is 5',
        validators=[MaxValueValidator(5)]
    )

    def __str__(self):
        return f'{self.date} {self.time} - {self.user.username}'
