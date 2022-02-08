from django import forms

class LoginForm(forms.Form):
    Username = forms.CharField()
    Password =forms.CharField()
