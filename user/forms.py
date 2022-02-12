from django import forms
from django.contrib import messages


class LoginForm(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField(widget=forms.PasswordInput)


class RegisterUserForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    repassword = forms.CharField()