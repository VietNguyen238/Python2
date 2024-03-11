from django.shortcuts import render
from .form import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib import messages

def index(request):
	return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')


def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/login')
    return render(request, "register.html", {"form": form})

def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return HttpResponseRedirect("/home")
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect("/")
    return render(request, "login.html")
def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return HttpResponseRedirect('/')
