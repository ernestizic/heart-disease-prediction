# Generated by Django 3.0.5 on 2020-09-13 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0021_symptom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='symptom',
            name='age',
        ),
    ]
