from django.urls import path
from .views import * 

urlpatterns = [
    path('',home,name="home"),
    path('register/',register,name="register"),
    path('login/',login,name="login"),
    path('nsebse/',nsebse,name='nsebse'),
    path('companies/',companies,name='companies'),
    path('notregistered/',notRegistered,name='notregistered'),
    path('profile/',profile,name='profile'),
]