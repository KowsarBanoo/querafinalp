from django.contrib import admin
from .models import Movie, FeedBack
# Register your models here.

class filmFilm(admin.ModelAdmin):
    model = Movie
    fields = ['title','creator']
    extra = 0
    # this is a decorator. we use decorators in the flask and django.

class feedbackFeedback(admin.ModelAdmin):
    list_display = ['id','title','text','created_at','updated_at']




admin.site.register(Movie,filmFilm)
admin.site.register(FeedBack,feedbackFeedback)
