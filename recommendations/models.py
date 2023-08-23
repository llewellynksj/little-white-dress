from django.db import models
from django.contrib.auth.models import User


class Recommendation(models.Model):
    TYPES = [
        ('Music', 'Music'),
        ('Vehicles', 'Vehicles'),
        ('Venues', 'Venues'),
        ('Photographers', 'Photographers'),
        ('Photobooths', 'Photobooths'),
        ('Decor', 'Decor'),
        ('Bridesmaid dresses', 'Bridesmaid dresses'),
        ('Accessories', 'Accessories'),
        ('Catering', 'Catering'),
    ]

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    type_of_recommendation = models.CharField(max_length=100, choices=TYPES)
    title = models.CharField(max_length=60)
    location = models.CharField(max_length=50, help_text='Please state the city or town')
    web_link = models.TextField(max_length=2000, default='www.google.com')
    summary = models.TextField(max_length=500, help_text="Tell us a bit about why you're recommending this service")
    date_posted = models.DateField(auto_now=True)
    posted_by = models.CharField(max_length=50, help_text='Enter your name, a username, or anonymous')

    def __str__(self):
        return self.title
