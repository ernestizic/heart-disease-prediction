# Generated by Django 3.0.5 on 2020-09-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0023_symptom_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptom',
            name='chest_pain_type',
            field=models.IntegerField(verbose_name=3),
        ),
    ]
