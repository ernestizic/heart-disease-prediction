from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from .forms import PatientCreationForm, SymptomForm
from .models import Patient, Symptom
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import numpy as np
import joblib


# Create your views here.

@login_required
def doctor_page(request):
    return render(request, 'doctors/doctor_page.html')


@login_required
def addpatient(request):
    if request.method == 'POST':
        patient_form = PatientCreationForm(request.POST)
        if patient_form.is_valid():
            patient_form.save()
            messages.success(request, "Patient creation successful.")
            return redirect('doctors:add-patient')
    else:
        patient_form = PatientCreationForm()
    return render(request, 'doctors/addpatient.html', {'patient_form': patient_form})


@login_required
def allpatients(request):
    patient_list = Patient.objects.all().order_by('name')
    # Search code
    query = request.GET.get('q')
    if query:
        patient_list = Patient.objects.filter(
            Q(name__icontains=query) |
            Q(pk__icontains=query)
        )

    # Search code ends
    page = request.GET.get('page', 1)
    paginator = Paginator(patient_list, 10)
    try:
        patients = paginator.page(page)
    except PageNotAnInteger:
        patients = paginator.page(1)
    except EmptyPage:
        patients = paginator.page(paginator.num_pages)
    return render(request, 'doctors/allpatients.html', {'patients': patients})


@login_required
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    model_path = 'ml_model/model.pkl'
    value = ''

    symptom_form = SymptomForm(request.POST or None)
    if request.method == 'POST':
        if symptom_form.is_valid():
            instance = symptom_form.save(commit=False)

            age = int(request.POST.get('age'))
            trestbps = int(request.POST.get('blood_pressure'))
            chol = int(request.POST.get('cholestoral_in_mg'))
            fbs = bool(request.POST.get('fasting_blood_sugar'))
            restecg = int(request.POST.get('electrocardiographic_result'))
            thalach = int(request.POST.get('maximum_heart_rate_achieved'))
            cp = int(request.POST.get('chest_pain_type'))

            user_data = np.array([[age, trestbps, chol, fbs, restecg, thalach, cp]]).reshape(1, 7)
            svc = joblib.load(open(model_path, 'rb'))
            prediction = svc.predict(user_data)
            if int(prediction[0]) == 1:
                value = 'POSITIVE'
            elif int(prediction[0]) == 0:
                value = 'NEGATIVE'

            instance.result = prediction[0]
            instance.save()
            symptom_form = SymptomForm()
            messages.success(request, "Prediction successful.")

    else:
        symptom_form = SymptomForm()

    context = {
        'patient': patient,
        'symptom_form': symptom_form,
        'val': value,
    }
    return render(request, 'doctors/patientdetail.html', context)


def prediction_result(request, patient_id):
    result = get_object_or_404(Symptom, pk=patient_id)
    return render(request, 'doctors/result.html', {'result': result})
