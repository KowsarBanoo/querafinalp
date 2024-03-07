from django.urls import path#arsalan
from .views import createc, retrievec, updatec, deletec, createm, retrievem, updatem, deletem, usersignup, userlogin, userlogout
urlpatterns= [
    path('new-critique/', createc, name='new-critique'),
    
    path("retrieve-critique/", retrievec, name="retrieve-critique"),
    
    path('update-critique/', updatec,name='update-critique'),
    
    path('delete-critique/', deletec ,name='delete-critique'),
    
    path('new-movie/', createm, name='new-movie'),
    
    path('retrieve-movie/', retrievem,name='retrieve-movie'),

    path('update-movie/', updatem, name='update-movie'),

    path('delete-movie/', deletem,name='delete-movie'),  

    path('usersignup/', usersignup,name='usersignup'),

    path('userlogin/', userlogin, name='userlogin'),

    path('userlogout/', userlogout, name='userlogout')
]
