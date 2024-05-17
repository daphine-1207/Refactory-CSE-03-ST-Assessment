from django import forms
from .models import Student


class StudentApplicationForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Student
        fields = [
            'first_name', 'last_name', 'course', 'entryscheme', 'intake', 'sponsorship', 'gender', 'date_of_birth', 'residence', 
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

        

