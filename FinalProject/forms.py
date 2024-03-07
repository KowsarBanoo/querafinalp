from djnango import forms
from .models import User

class RegisterForm(forms.ModelsForm):
    class Meta:
        model = User
        fields = ["username", "email", "password"]

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]