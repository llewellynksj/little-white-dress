from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Category model links to the Product Model
    Each Product belongs to a Category
    """
    category_image = CloudinaryField('image', default='placeholderCategory')
    category_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    """
    Product models holds all information relating to products
    """
    main_image = CloudinaryField('image', default='placeholderProduct')
    item_name = models.CharField(max_length=50, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    description = models.TextField(
        default='Contact us to find out more about this gown',
        blank=True,
        max_length=2000)
    colours = models.TextField(default='Ivory', blank=True, max_length=500)
    sizes_avail = models.TextField(
        default='8 - 26', blank=True, max_length=500)
    likes = models.ManyToManyField(
        User, related_name='fav_products', blank=True)

    def __str__(self):
        return self.item_name
