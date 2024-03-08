from django import forms
from .models import UserModel, Movie, FeedBack

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["username", "email", "password"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["username", "password"]

class updatemForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields= ["title","text"]

class MovieForm(forms.ModelForm):#arsalan
    class Meta:
        model = Movie
        fields = ['title','text']

class UpdateFeedBackFrom(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['movie','personal_feedback']
