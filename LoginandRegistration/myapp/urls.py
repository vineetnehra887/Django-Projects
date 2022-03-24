from django.contrib import admin
from django.urls import path
from myapp import views


 
urlpatterns = [    
    path('',views.home),
    path('login/',views.loginuser),
    path('register/',views.registeruser),
    path('logout',views.logoutuser, name="logout"),
    

]  
