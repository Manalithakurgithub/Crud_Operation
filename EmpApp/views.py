from django.shortcuts import render,redirect
from .models import Emp,EmpForm
from django.views.generic import View
# Create your views here.
def home(request):
    return render(request,'home.html')

def add_emp(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        address=request.POST.get('address')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        e=Emp()
        e.fname=fname
        e.lname=lname
        e.address=address
        e.email=email
        e.phone=phone
        e.age=age
        e.save()
        return redirect('/')      
    else:
        return render(request,'addemp.html')

def view_emp(request):
    elist=Emp.objects.all()
    d={'el':elist}
    return render(request,'viewemp.html',d)

def delete_emp(request,id):
    emp=Emp.objects.get(id=id)
    emp.delete()
    return redirect('/') 

def edit_emp(request,id):
    emp=Emp.objects.get(id=id)
    return render(request,'edit.html',{'emp':emp})

def do_edit_emp(request,id):
    fname=request.POST.get('fname')
    lname=request.POST.get('lname')
    address=request.POST.get('address')
    email=request.POST.get('email')
    phone=request.POST.get('phone')
    age=request.POST.get('age')

    emp=Emp.objects.get(id=id)
    emp.fname=fname
    emp.fname=fname
    emp.address=address
    emp.email=email
    emp.phone=phone
    emp.age=age
    emp.save()
    return redirect('/')  
