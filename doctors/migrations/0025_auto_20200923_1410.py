# Generated by Django 3.0.5 on 2020-09-23 13:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0024_auto_20200923_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptom',
            name='chest_pain_type',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(3)]),
        ),
    ]
