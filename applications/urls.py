from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', homePage, name= 'home'),
    path('register/', register, name= 'register'),
  
]


