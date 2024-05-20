from django import forms
from django import views
from .models import *
from django import forms
from django.core.exceptions import ValidationError
from datetime import date
class Userform(forms.ModelForm):
      Date_of_Birth= forms.DateField( required=True , widget=forms.widgets.TextInput(attrs={"label":"Date_of_birth", "placeholder":"(YYY/MM/DD) ", "class":"form-control"}),)
      class Meta():
            model =User
            fields = '__all__'