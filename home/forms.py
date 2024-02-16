from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Seleruser,Product
from django.contrib.auth.models import User
from django.db import models

class selerusersignupform(UserCreationForm):
    companyname = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    fieldproduct = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username','companyname', 'city', 'fieldproduct', 'first_name', 'last_name', 'password1', 'password2']

class addproductform(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = Product
        fields = ['name', 'description','price']
       