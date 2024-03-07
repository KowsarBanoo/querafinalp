from django.urls import path
from .views import usersignup, userlogin, userlogout

urlpatterns= [
    path('new-critic/', )
    path('signup/', usersignup, name='register'),
    path('login/', userlogin, name='login'),
    path('logout/', userlogout, name='logout')
]