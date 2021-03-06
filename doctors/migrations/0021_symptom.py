# Generated by Django 3.0.5 on 2020-09-08 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0020_delete_symptom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='doctors.Patient')),
                ('age', models.IntegerField()),
                ('chest_pain_type', models.IntegerField()),
                ('blood_pressure', models.IntegerField()),
                ('cholestoral_in_mg', models.IntegerField()),
                ('fasting_blood_sugar', models.BooleanField()),
                ('electrocardiographic_result', models.BooleanField()),
                ('maximum_heart_rate_achieved', models.IntegerField()),
            ],
        ),
    ]
