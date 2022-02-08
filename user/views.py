from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from  .forms import LoginForm

def user_login(request):
    if request.method=="POST":
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
        form=LoginForm()
    return render(request, "login.html", {"form":form})