from django.db import models

# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_field = models.EmailField(unique=True)
    phone = models.IntegerField()
    address = models.TextField()
    date_of_birth = models.DateField()
    
    
class Stock(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price =models.DecimalField(max_digits=20,decimal_places=2)
    stock_quantity = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    