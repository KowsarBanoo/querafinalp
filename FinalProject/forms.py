from django import forms
from .models import User, movie

class RegisterForm(forms.ModelsForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]

class updatemForm(forms.modelform):
    class Meta:
        model = movie
        fields = ["title","text"]

class MovieForm(forms.ModelForm):#arsalan
    class Meta:
        model = movie
        fields = ['title','text']
