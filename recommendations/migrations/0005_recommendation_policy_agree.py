# Generated by Django 3.2.20 on 2023-08-28 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0004_alter_recommendation_type_of_recommendation'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='policy_agree',
            field=models.BooleanField(default=False),
        ),
    ]
