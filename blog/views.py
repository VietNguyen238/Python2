from django.shortcuts import render
from .models import Post
from .form import RegistrationForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.contrib import messages


# Create your views here.

def list(request):
    Data = {"Posts": Post.objects.all().order_by("-date")}
    return render(request, "pages/blog.html", Data)


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "pages/post.html", {"post": post})

def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/login')
    return render(request, "pages/register.html", {"form": form})

def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return HttpResponseRedirect("/blog")
        else:
            messages.error(request, "Invalid Credentials")
            return HttpResponseRedirect("/blog/login")
    return render(request, "pages/login.html")
def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return HttpResponseRedirect('/blog/login')
