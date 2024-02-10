from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Seleruser,Product

class selerusersignupform(UserCreationForm):
    companyname = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    fieldproduct = forms.CharField(max_length=100)
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Seleruser
        fields = ['username','companyname', 'city', 'fieldproduct', 'firstname', 'lastname', 'password1', 'password2']

class addproductform(forms.ModelForm):
    name = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        model = Product
        fields = ['name', 'description','price']
       