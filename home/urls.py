from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path('login/',views.loginuser,name='login'),
    path('logout/',views.logoutuser,name='logout'),
    path('register/', views.register, name='register'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
    path("cart/",views.cart,name='cart'),
    path("checkout/",views.checkout,name='checkout'),
    path('search/',views.search, name='search'),
    
]