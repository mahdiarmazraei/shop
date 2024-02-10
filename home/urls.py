from django.urls import path

from . import views


# app_name='home'
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
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('selerusersignup/', views.selerusersignup, name='selerusersignup'),
    path('addproduct/', views.addproduct, name='addproduct'),



]