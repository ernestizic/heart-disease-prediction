# Generated by Django 3.0.5 on 2020-09-19 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0022_remove_symptom_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='symptom',
            name='age',
            field=models.IntegerField(default=25),
            preserve_default=False,
        ),
    ]
