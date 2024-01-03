from django.shortcuts import render,redirect
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login,authenticate,logout
from .models import reg
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm




@login_required(login_url='signin')
def home(request):
    return render(request,'home2/home2.html')
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'home2/home2.html')
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
            return render(request, 'home2/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'home2/login.html', {'form': form})
@login_required(login_url='signin')
def profile(request):
    return render(request,'home2/profile.html')
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
            return render(request, 'home2/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'home2/signup.html', {'form': form})
   
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

