from django.urls import path
from .views import *

urlpatterns = [
    path('my-feedbacks/<int:pk>/', RetrieveMyFeedBackView.as_view())
]
