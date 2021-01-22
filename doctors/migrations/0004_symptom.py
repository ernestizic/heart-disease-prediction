# Generated by Django 3.0.5 on 2020-09-06 00:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_patient_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('chest_pain_type', models.IntegerField()),
                ('blood_pressure', models.IntegerField()),
                ('cholestoral_in_mg', models.IntegerField()),
                ('fasting_blood_sugar', models.BooleanField()),
                ('electrocardiographic_result', models.BooleanField()),
                ('maximum_heart_rate_achieved', models.IntegerField()),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='doctors.Patient')),
            ],
        ),
    ]