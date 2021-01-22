from django import forms
from .models import Patient, Symptom


class PatientCreationForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Surname and Other Names'}))
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'year-month-day'}))

    class Meta:
        model = Patient
        fields = ('name', 'sex', 'date_of_birth', 'phone')


""""
class PatientEditForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    date_of_birth = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly'}))

    class Meta:
        model = Patient
        fields = ('name', 'date_of_birth',)
"""


class SymptomForm(forms.ModelForm):
    class Meta:
        model = Symptom
        exclude = ('result',)
