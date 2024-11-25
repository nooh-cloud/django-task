from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(max_length=120)
    price = models.IntegerField()
    stock_quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=30)
    product = models.CharField(max_length=20)
    quantity = models.IntegerField()
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=[('pending','pending'),('shipped','shipped'),('delivered','delivered')])
    
    
class User(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    place = models.CharField(max_length=50)
    
    
    
class login(models.Model):
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=8)
    
    
class book(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    author = models.CharField(max_length=50)
    
    
class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    
    
class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=8,decimal_places=2)
    