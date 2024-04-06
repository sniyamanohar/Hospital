from django import forms
from.models import Patient,Appointment,Doctor,login



class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields="__all__"
        widgets={
        
    }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
        widgets = {

                }

class appointmentForm(forms.ModelForm):
    class Meta:
        model=Appointment
        fields="__all__"
        widgets={


        }

class loginForm(forms.ModelForm):
    class Meta:
        model=login
        fields="__all__"
        widgets={


        }