from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User
import datetime
from datetime import datetime


class Appointment(models.Model):
    """
    Appointment Model reflects database of booked appointments
    Links to MakeBookingForm
    """
    TIME_SLOTS = [
        ('09:00', '09:00'),
        ('11:30', '11:30'),
        ('14:00', '14:00'),
        ('16:30', '16:30'),
    ]

    # Raises validation error if user has selected a day the store is closed
    def validate_weekday(booking_date):
        date = booking_date.weekday()
        if date == 5 or date == 6:
            raise ValidationError(
                "LWD is not open at the weekend. Please choose another day")

    # Rasies validation error if the user has selected a date in the past
    def validate_future_date(booking_date):
        if booking_date < datetime.today().date():
            raise ValidationError('Date cannot be in the past')

    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE
    )
    booking_date = models.DateField(
        validators=[validate_weekday, validate_future_date],
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

    class Meta:
        """
        Metadata Class Container
        Checks the booking date and time are not already booked
        """
        unique_together = ('booking_date', 'time')
        ordering = ["booking_date"]

    def __str__(self):
        return f'{self.date} {self.time} - {self.user.username}'
