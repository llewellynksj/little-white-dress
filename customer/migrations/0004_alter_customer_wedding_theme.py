# Generated by Django 3.2.20 on 2023-09-23 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20230923_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='wedding_theme',
            field=models.CharField(blank=True, help_text='e.g. rustic, winter, art deco', max_length=200, null=True),
        ),
    ]
