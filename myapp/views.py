from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def read(request):
    x = Customer.objects.all()
    
    return render(request,'read.html',{'data':x})

def create(request):
    if request.method == 'POST':
        name1 = request.POST['names']
        name2 = request.POST['namess']
        email1 = request.POST['emaill']
        phone1 = request.POST['phones']
        address1 = request.POST['addresss']
        date1 = request.POST['births']
        Customer.objects.create(first_name = name1,last_name = name2,email_field = email1,phone= phone1,address = address1,date_of_birth = date1)
        
        return redirect('read1') 
    return render(request,'form.html')

def update(request,id):
    user = Customer.objects.get(id=id)
    if request.method == 'POST':
        name1 = request.POST['names']
        name2 = request.POST['namess']
        email1 = request.POST['emaill']
        phone1 = request.POST['phones']
        address1 = request.POST['addresss']
        date1 = request.POST['births']
        user.first_name = name1
        user.last_name = name2
        user.email = email1
        user.phone = phone1
        user.address = address1
        user.date_of_birth = date1
        user.save()    
        return redirect('read1')
    return render(request,'update.html',{'data':user})

def delete(request,id):
    user = Customer.objects.get(id=id)
    user.delete()
    return redirect('read1')




def read1(request):
    x = Stock.objects.all()
    
    return render(request,'read1.html',{'data':x})



def create1(request):
    if request.method == 'POST':
        name1 = request.POST['names']
        description1 = request.POST['descriptions']
        price1 = request.POST['prices']
        stock1 = request.POST['stocks']
        create1 = request.POST['creates']
        Customer.objects.create(name = name1,description = description1,price = price1,stock_quantity = stock1,created = create1)
        
        return redirect('read2') 
    return render(request,'form1.html')


def update1(request,id):
    user = Stock.objects.get(id = id)
    if request.method == 'POST':
        name1 = request.POST['names']
        description1 = request.POST['descriptions']
        price1 = request.POST['prices']
        stock1 = request.POST['stocks']
        create1 = request.POST['creates']
        user.name = name1
        user.description = description1
        user.price = price1
        user.stock_quantity = stock1
        user.created = create1
        user.save()    
        return redirect('read2')
    return render(request,'update1.html',{'data':user})    
        
        
def delete1(request,id):
    user = Stock.objects.get(id=id)
    user.delete()
    return redirect('read2')