from django.urls import path

from . import views

urlpatterns = [
    # path('home', views.HomeView.as_view()),
    # path('authorized', views.AuthorizedView.as_view()),
    # path('login', views.LoginInterfaceView.as_view(), name='login'),
    # path('',views.HomeView.as_view(), name='home'),
    # path('logout', views.LogoutInterfaceView.as_view()),
    # path("user_login/",views.user_login, name='user_login')
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('profile/',views.profile,name='profile'),
    path('signout/',views.signout,name='signout'),
    path('signin/',views.signin,name='signin'),


]