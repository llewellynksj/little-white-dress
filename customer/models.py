from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Customer(models.Model):
    """
    Custom model to provide additional profile details for customer
    """
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = CloudinaryField('image', default='placeholder')
    date_of_wedding = models.DateField(blank=True, null=True)
    partners_name = models.CharField(max_length=50, null=True, blank=True)
    wedding_location = models.CharField(max_length=200, blank=True, null=True)
    wedding_theme = models.CharField(
        max_length=200,
        null=True, blank=True,
        help_text='e.g. rustic, winter, art deco')
    website_url = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse('index')
