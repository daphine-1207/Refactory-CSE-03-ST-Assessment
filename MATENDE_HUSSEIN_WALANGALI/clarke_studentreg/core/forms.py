from django import forms
from .models import *

class StudentRegForm(forms.ModelForm):
    class Meta:
        model = StudentReg
        fields = [
            'f_name','l_name','course','entry_scheme','intake','sponsorship','gender','dob','residence'
        ]
        widgets = {
            'gender': forms.RadioSelect(),
        }