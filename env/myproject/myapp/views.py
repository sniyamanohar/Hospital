from django.shortcuts import render,redirect
from.models import Patient,Appointment,Doctor
from.forms import appointmentForm,PatientForm,DoctorForm
from django.contrib.auth.models import User,auth
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')


#appointment function code

def appointment(request):
    if request.method=="POST":
        form=appointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"home.html")

    else:
        form=appointmentForm()
        return render(request,'appointment.html')









    #patient function code
'''def patientregistration(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                return redirect('patientregistration')
            user=User.objects.create_user(username=username,password=password)
            user.save()
                #print("user created")
        else:
            return  redirect('patientregistration')
        return redirect('/')
    else:
        return render(request,'patientregistration.html')'''

def doctorlist(request):
    return render(request,'doctorlist.html')




def patientregistration(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                return redirect('patientregistration')  # Redirect to registration if username exists
            user = User.objects.create_user(username=username, password=password)
            user.save()
            # Redirect to a different URL upon successful registration
            return redirect('/')
        else:
            return redirect('patientregistration')  # Redirect to a page indicating password mismatch
    else:
        return render(request, 'patientregistration.html')


def doctorregistration(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        password1=request.POST["password1"]
        if password==password1:
            if User.objects.filter(username=username).exists():
                return redirect('doctorregistration')
            user=User.objects.create_user(username=username,password=password)
            user.save()
        else:
            return redirect('doctorregistration')
        return redirect('/')
    else:
        return render(request,'doctorregistration.html')

def base(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def login(request):
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        try:
            user=Patient.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'usermodule.html')
            return render(request,'login.html')



        except:
            pass
        try:
            user=Login.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request, 'home.html')
                #return
                #render(request,'adminmodule.html')
        except:
            pass
        try:
            user=Doctor.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'Doctormodule.html')
            return render(request, 'home.html')


        except:
            pass
    else:
        return render(request,'login.html')


def usermodule(request):
    return render(request, 'usermodule.html')
def Doctormodule(request):
    return render(request, 'Doctormodule.html')
def approveapoiment(request):
    return HttpResponse("<h1> please wait for your appointment </h1>")
def viewappointment(request):
    return render(request, 'viewappointment.html')







