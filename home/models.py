from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group, Permission

class Seleruser(AbstractUser):
    companyname = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    fieldproduct = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'seleruser'

    def __str__(self):  
        return self.username
    empAuth_object = models.Manager()

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # image = models.ImageField(upload_to='static/image')
    seler = models.ForeignKey(Seleruser, on_delete=models.CASCADE,default=1)


    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name
class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    total_price = models.PositiveIntegerField(default=0)
    

    class Meta:
        db_table = 'cartitem'
 



        
