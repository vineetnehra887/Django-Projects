from django.contrib import admin
from django.urls import path
from myapp import views


 
urlpatterns = [    
    path('', views.index, name="home"),
    path('view', views.show_file, name="view")
]