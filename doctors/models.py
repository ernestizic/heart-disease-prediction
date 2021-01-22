from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from datetime import date, datetime

# Create your models here.


GENDER_CHOICES = (
    ('Male', 'M'),
    ('Female', 'F'),
)


class Patient(models.Model):
    name = models.CharField(max_length=250)
    sex = models.CharField(choices=GENDER_CHOICES, max_length=6, default='Male')
    date_of_birth = models.DateField(blank=False, null=True)
    phone = models.CharField(max_length=11, default='08000000000')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('doctors:patient_detail', args=[self.id])

    @property
    def age(self):
        return int((datetime.now().date() - self.date_of_birth).days / 365.25)


class Symptom(models.Model):
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField()
    chest_pain_type = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(3)])
    blood_pressure = models.IntegerField()
    cholestoral_in_mg = models.IntegerField()
    fasting_blood_sugar = models.BooleanField()
    electrocardiographic_result = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(2)])
    maximum_heart_rate_achieved = models.IntegerField()
    result = models.CharField(max_length=20, default='No Result')

    def __str__(self):
        return self.patient.name


"""
from doctors.models import Patient
>>> p1 = Patient(id=1, name="Akinwole Akin Kayode")
>>> p1.save()
"""