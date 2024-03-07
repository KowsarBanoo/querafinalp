from django import forms 
from .models import user# یه چیز دیگه باید ایمپورت بشه و مدل هم یه چیزی داره

class MovieForm(forms.ModelForm):
    class Meta:
        # model = 
        fields = ['title','text']