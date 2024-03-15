from django import forms
from .models import UserModel, Movie, FeedBack

class RegisterForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["username", "email", "password"]

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class updatemForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields= ["title","text","creator"] #in details roehtemalan bayad dar model biarim

class MovieForm(forms.ModelForm):#arsalan
    class Meta:
        model = Movie
        fields = ['title','text']

class UpdateFeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ['movie','personal_feedback']
