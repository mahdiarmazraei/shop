from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login,authenticate,logout
from .models import Product,CartItem,Seleruser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from os.path import basename
from .forms import selerusersignupform,addproductform

def addproduct(request):
    if request.method == 'POST':
        form = addproductform(request.POST, request.FILES)
        if form.is_valid():
            # اینجا فروشنده فعلی به عنوان فروشنده محصول ذخیره می‌شود
            form.instance.seler = Seleruser.objects.get(id=request.user.id)
            form.save()
            return redirect('/')  # مسیر به لیست محصولات
    else:
        form = addproductform()
    return render(request, 'home2/addproduct.html', {'form': form})

def selerusersignup(request):
    if request.user.is_authenticated:
        return redirect('/')    
    if request.method == 'POST':
        form = selerusersignupform(request.POST)
        if form.is_valid():
            user = form.save()
            authenticated_user = authenticate(username=user.username, password=form.cleaned_data['password1'])
            if authenticated_user is not None:
                login(request, authenticated_user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('/')
    
            # username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=password)
            # login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            # می‌توانید به هر صفحه‌ای که دوست دارید منتقل شوید
    else:
        form = selerusersignupform()

    return render(request, 'home2/selerusersignup.html', {'form': form})

def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'home2/index.html', {'cart_items': cart_items, 'total_price': total_price})
 
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.total_price += cart_item.product.price
    cart_item.save()
    return redirect('view_cart')
 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.quantity -= 1
    cart_item.save()
    if cart_item.quantity==0:
        cart_item.delete()
    return redirect('view_cart')
def home(request):
    products = Product.objects.all()
    return render(request,'home2/home2.html',{'products':products})
def signin(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        return render(request,'home2/home2.html',{'products':products})
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'home2/logintest.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'home2/logintest.html', {'form': form})
@login_required(login_url='signin')
def profile(request):
    account = request.user
    context={}
    context['user']=account
    return render(request,'home2/profile.html',{'user':account})
    # return render(request,'home2/profile.html')
def signout(request):
    logout(request)
    return redirect('/')
def signup(request):
    if request.user.is_authenticated:
        return redirect('/')    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
        else:
            return render(request, 'home2/signuptest.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'home2/signuptest.html', {'form': form})
   
# class LogoutInterfaceView(LogoutView):
#     template_name = 'home/logout.html'


# class LoginInterfaceView(LoginView):
#     template_name = 'home/login.html'
# def user_login(request):

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             user = reg.empAuth_object.get(username=username, password=password)
#             if user is not None:
#                 return render(request,'home/home.html',{})
#             else:
#                 print("someone tried to login and failed.")
#                 print("used{}{}".format(username,password))
#                 return redirect('home/send.html')

#         except Exception as identifier:

#             return redirect('home/send.html')


#     else:
#         return render(request,'home/login.html')
    
# @login_required(login_url='home/login.html')
# class HomeView(LoginRequiredMixin,TemplateView):
    # login_url = "home/login.html"
    # redirect_field_name = "home/login.html"
    # template_name = 'home/home.html'

