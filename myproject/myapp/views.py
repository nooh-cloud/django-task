from django.shortcuts import render
from .models import *
# Create your views here.


def hello(request):
    x = Product.objects.all()
    
    return render(request,'read.html',{'data':x})


def hi(request):
    y = Order.objects.all()
    return render(request,'read2.html',{'data':y})


def task(request):
    a = [{"name":"Laptop","price":999.9,"status":True},
         {"name":"smartphone","price":999.9,"status":False},
         {"name":"Tablet","price":299.9,"status":True},
         {"name":"Headphones","price":149.9,"status":True},]
    
    return render(request,"task1.html",{"data":a})


def read(request):
    b = User.objects.all()
    return render(request,"read.html",{"data":b})

def readbook(request):
    datas = book.objects.all()
    return render(request,"reaad.html",{"data":datas})

def cust(request):
    d = Customer.objects.all()
    return render(request,"cust.html",{"data":d})

def emp(request):
    e = Employee.objects.all()
    return render(request,"empl.html",{"data":e})