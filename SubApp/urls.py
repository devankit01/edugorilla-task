from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name = 'index'),
    path('auth/profile', profile, name = 'profile'),

    path('auth/signup/' , signup , name = 'signup'),
    path('auth/logout/' , logout , name = 'logout'),
    path('auth/signin/' , signin , name = 'signin'),
    path('<slug>/' , article , name = 'article'),
    path('likes/<slug>', likesPost, name = 'likesPost'),
]
