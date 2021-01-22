from django.contrib import admin
from .models import Patient, Symptom


# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'sex', 'phone')
    search_fields = ('name',)


admin.site.register(Patient, PatientAdmin)
admin.site.register(Symptom)
