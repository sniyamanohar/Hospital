from django.db import models

# Create your models here.
class Patient(models.Model):
    patientname=models.CharField(max_length=150)
    dob=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    gender=models.CharField(max_length=100)
    username=models.CharField(max_length=150,null=True,blank=True)
    password=models.CharField(max_length=150,null=True,blank=True)
    password1=models.CharField(max_length=150,null=True,blank=True)

    def __str__(self):
        return self.patientname

class Appointment(models.Model):
    patientname=models.CharField(max_length=150)
    doctorname=models.CharField(max_length=150)
    appointmentdate=models.CharField(max_length=150)
    symptoms=models.CharField(max_length=150)
    def __str__(self):
        return self.patientname

class Doctor(models.Model):
    doctorname=models.CharField(max_length=150)
    dob=models.CharField(max_length=200)
    address=models.CharField(max_length=200)
    specialization=models.CharField(max_length=150)
    contact=models.CharField(max_length=200)
    username=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    password1=models.CharField(max_length=150)
    def __str__(self):
        return self.doctorname


class login(models.Model):
    username=models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    def __str__(self):
        return self.username


