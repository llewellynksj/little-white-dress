# Generated by Django 3.2.20 on 2023-09-21 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_of_wedding',
            field=models.DateField(blank=True, null=True),
        ),
    ]
