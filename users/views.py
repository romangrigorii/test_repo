from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
    if not request.user.is_authenticated: # checks if the user has been logged in already or not. If not, we just go to the login page
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html") # if the user is authenticated then we go to their page

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("users:index")) # reverse utilized the name of the page to go to the url associated with it 
        else:
            return render(request,"users/login.html",{
                "message": "Invalid credentials"
            })

    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "message": "logged out."
    })