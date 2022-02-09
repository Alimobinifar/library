from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from  .forms import LoginForm, RegisterUserForm


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            Username = form.cleaned_data['Username']
            Password = form.cleaned_data["Password"]
            user = authenticate(username=Username, password=Password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                pass
    else:
        form = LoginForm()
    return render(request, "login.html", {"form":form})


def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('home')
    else:
        pass

def user_register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if data['password'] == data['repassword']:
                user = User.objects.create_user(data['username'], data['email'], data['password'])
                user.save()
                return HttpResponse("OK Shoma sabt nam shodi ")
            else:
                return HttpResponse("passwords are not match together ")
    else:
        form = RegisterUserForm()
    return render(request, "register.html", {"form": form})