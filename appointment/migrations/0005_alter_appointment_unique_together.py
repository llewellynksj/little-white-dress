# Generated by Django 3.2.20 on 2023-09-19 08:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_auto_20230919_0820'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='appointment',
            unique_together={('booking_date', 'time')},
        ),
    ]