from django.shortcuts import render,redirect
from .models import *
# Create your views here.


def read(request):
    x = Customer.objects.all()
    
    return render(request,'read.html',{'data':x})

def create(request):
    if request.method == 'POST':
        firstname1 = request.POST.get('names')
        lastname1 = request.POST.get('namess')
        email1 = request.POST.get('emaill') 
        phone1 = request.POST.get('phones')
        address1 = request.POST.get('addresss')
        date_of_birth1 = request.POST.get('births')
        Customer.objects.create(
            first_name=firstname1,
            last_name=lastname1,
            email_field=email1, 
            phone=phone1,
            address=address1,
            date_of_birth=date_of_birth1
        )
        return redirect('read1')
    return render(request, 'form.html')
