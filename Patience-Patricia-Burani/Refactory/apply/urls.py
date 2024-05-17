from django.urls import path
from . import views

urlpatterns = [
    path('add_register/', views.add_register, name='add_register'),
 
]
