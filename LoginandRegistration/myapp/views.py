from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login 
from django.contrib.auth.models import User,auth
# Create your views here.


def registeruser(request):
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
 
def loginuser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')
 
def home(request):
    print(request.user)
    """if request.user.is_anonymous:
        return redirect("/")""" 
    return render(request, 'home.html')

def logoutuser(request):
    print('logged out')
    logout(request)

    return redirect('/login')
