from django.urls import path#arsalan
from .views import createc, RetrieveMyFeedBackView, UpdateMyFeedBackView, deletec, createm, retrievem, updatem, deletem, usersignup, userlogin, userlogout
urlpatterns= [
    path('new-critique/', createc, name='new-critique'),
    
    path('my-feedbacks/<int:pk>/', RetrieveMyFeedBackView.as_view()),
    
    path('my-feedbacks/update/<int:pk>/', UpdateMyFeedBackView.as_view() ,name='update-critique'),
    
    path('delete-critique/<int:id>/', deletec ,name='delete-critique'),
    
    path('new-movie/', createm, name='new-movie'),
    
    path('retrieve-movie/<int:id>/', retrievem,name='retrieve-movie'),

    path('update-movie/<int:id>/', updatem, name='update-movie'),

    path('delete-movie/<int:id>/', deletem,name='delete-movie'),  

    path('usersignup/', usersignup,name='usersignup'),

    path('userlogin/', userlogin, name='userlogin'),

    path('userlogout/', userlogout, name='userlogout')
]
