from django.contrib import admin
from django.urls import path
from myapp import views


 
urlpatterns = [    
    path('',views.home),
    #path('home/',views.home),
    path('login/', views.login_user, name ='login'),
    path('register/',views.registerUser),
    path('logout',views.logoutUser, name="logout"),
    

]  
