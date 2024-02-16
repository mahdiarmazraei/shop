from django.contrib import admin
from .models import Product, CartItem,Seleruser

 
admin.site.register(CartItem)
admin.site.register(Product)
admin.site.register(Seleruser)
