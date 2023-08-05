from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Category(models.Model):
    category_image = CloudinaryField('image', default='placeholderCategory')
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name
