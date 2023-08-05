# Generated by Django 3.2.20 on 2023-08-05 11:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='fav_products', to=settings.AUTH_USER_MODEL),
        ),
    ]
