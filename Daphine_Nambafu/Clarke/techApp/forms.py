from django.forms import Form
from django import forms
from .models import *


#models here

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
