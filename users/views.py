from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.db import IntegrityError
from django.urls.base import reverse

from .models import User
# Create your views here.

success_redirect = 'base:homepage'
print(success_redirect)

def register_view(request):
    template = "users/register.html"
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, template, {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create(username=username, email=email, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse(success_redirect))
        #if error return form with message    
        except IntegrityError:
            return render(request, template, {
                "message": "Username already taken."
            })
        


    else:
        return render(request, template)

def login_view(request):
    template = "users/login.html"

    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        # Check if authentication successful
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse(success_redirect))
        else:
            return render(request, template, {
                "message": "Invalid username and/or password."
            })
            
    #GET
    else:
        return render(request, template)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse(success_redirect))