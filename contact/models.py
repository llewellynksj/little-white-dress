from django.db import models


class ContactDetail(models.Model):
    first_line_of_address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=50)
    postcode = models.CharField(max_length=15)
    telephone = models.PositiveBigIntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.first_line_of_address


class Enquiry(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=800)

    def __str__(self):
        return str('Message from' + self.full_name)
