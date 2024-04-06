"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('base', views.base, name='base'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),

    path('patientregistration', views.patientregistration, name='patientregistration'),
    path('doctorregistration', views.doctorregistration, name='doctorregistration'),

    path('appointment',views.appointment,name='appointment'),
    path('doctorlist', views.doctorlist, name='doctorlist'),
    path('login',views.login,name='login'),
    path('Doctormodule',views.Doctormodule, name='Doctormodule'),
    path('usermodule', views.usermodule, name='usermodule'),
    path('approveapoiment',views.approveapoiment,name='approveapoiment'),
    path('viewappointment', views.viewappointment, name='viewappointment')


]
