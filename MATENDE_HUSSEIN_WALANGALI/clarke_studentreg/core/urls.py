from django.urls import path
from . import views


urlpatterns = [
    path('', views.studentReg, name='student_reg')
]
