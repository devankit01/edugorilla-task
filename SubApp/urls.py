from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name = 'index'),
    path('auth/signup/' , signup , name = 'signup'),
    path('auth/signin/' , signin , name = 'signin'),
    path('<slug>/' , article , name = 'article'),
]
