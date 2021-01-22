from django.urls import path, re_path
from .import views

app_name = 'doctors'

urlpatterns = [
    path('', views.doctor_page, name='doctor_page'),
    path('add-patient/', views.addpatient, name="add-patient"),
    path('all-patients/', views.allpatients, name="all-patients"),
    path('<int:patient_id>/', views.patient_detail, name="patient_detail"),

    path('<int:patient_id>/result/', views.prediction_result, name="prediction_result"),
]
