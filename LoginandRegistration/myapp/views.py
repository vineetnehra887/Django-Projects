from email import message
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
# Create your views here.

def home(request):
    print(request.user)
    """if request.user.is_anonymous:
        return redirect("/loginuser")"""
    return render(request, 'home.html')

def login_user (request):
	if request.method == 'POST': #if someone fills out form , Post it 
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:# if user exist
			login(request, user)
			messages.success(request,('Youre logged in'))
			return redirect('/') #routes to 'home' on successful login  
		else:
			messages.success(request,('Error logging in'))
			return redirect('/login') #re routes to login page upon unsucessful login
	else:
		return render(request,'login.html', {})


def registerUser(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']

        user=User.objects.create_user(username=username, password=password, first_name=firstname, last_name=lastname)
        user.save()
        print("user created")
        return redirect('/login')

    else:
        return render(request, 'register.html')
 

 


def logoutUser(request):
    print('logged out')
    logout(request)

    return redirect('/login')
