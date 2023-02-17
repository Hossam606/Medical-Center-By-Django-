from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def home(request):   
          
    if request.method=="POST":
        dataform2=Message_form(request.POST)
        if dataform2.is_valid():
           dataform2.save() 


    context={
        'doctors':Doctor.objects.all,
        'f2':Message_form(), 
    }            

    return render(request,'pages/home.html' ,  context) 

def doctor(request): 
     context={
        'category':Department.objects.all,
        'doctors':Doctor.objects.all,
     }
     return render(request,'pages/doctors.html',context)


def department(request):
    context={
        'departments' :Department.objects.all,
    }
    return render(request,'pages/departments.html',context)


def appointment(request):

    if request.method == 'POST':
        add_appointment=Registration_form(request.POST)
        if add_appointment.is_valid():
            add_appointment.save()

    context={
        'f1':Registration_form(),
    }
    
    return render(request,'pages/Appointment.html',context)

def list(request):
     context={'list':Registration.objects.all()}
     return render(request,'pages/List.html',context)

def DoctorDate(request,name):
    
    NameDoctor=Registration.objects.get(Doctor_name=name)
    date=Registration_form(instance=NameDoctor)

    context={'list':date}
    return render(request,'pages/DoctorDate.html',context)