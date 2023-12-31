from django.db import models
from django.core.validators import EmailValidator


class ContactDetail(models.Model):
    """
    ContactDetail model allows admin to add and
    update store address, phone number and email address
    """
    first_line_of_address = models.CharField(
        max_length=200)
    second_line_address = models.CharField(
        max_length=200,
        default='Enter second line of address')
    city = models.CharField(
        max_length=50)
    county = models.CharField(
        max_length=50)
    postcode = models.CharField(
        max_length=15)
    telephone = models.PositiveBigIntegerField()
    email = models.EmailField(
        validators=[EmailValidator])
    monday_opening_hrs = models.CharField(
        max_length=1000,
        blank=True,
        null=True)
    tuesday_opening_hrs = models.CharField(
        max_length=1000,
        blank=True,
        null=True)
    wednesday_opening_hrs = models.CharField(
        max_length=1000,
        blank=True,
        null=True)
    thursday_opening_hrs = models.CharField(
        max_length=1000,
        blank=True,
        null=True)
    friday_opening_hrs = models.CharField(
        max_length=1000,
        blank=True,
        null=True)
    saturday_opening_hrs = models.CharField(
        max_length=1000,
        blank=True,
        null=True)
    sunday_opening_hrs = models.CharField(
        max_length=1000,
        blank=True,
        null=True)

    def __str__(self):
        return self.first_line_of_address


class Enquiry(models.Model):
    """
    Enquiry model saves contact form submissions
    """
    full_name = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator])
    message = models.TextField(max_length=800)

    def __str__(self):
        return self.full_name
