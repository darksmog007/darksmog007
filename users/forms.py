from django import forms


class Loginform(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())


class Signupform(forms.Form):
    name = forms.CharField(max_length=200)
    age = forms.CharField(max_length=200)
    address = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())