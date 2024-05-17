from django import forms

from .models import *

class RegisterForm(forms.ModelForm):
    COURSE = (
        ('Certificate in Health Science', 'Cerficate in Health Science'),
        ('Certificate in Applied Technology', 'Cerficate in Applied Technology'),
        ('Bachelors of Information Technology', 'Bachelors in Information Technology'),
        ('Bachelors in Business Technology', 'Bachelors in Business Technology'),
        ('Master of Public Health', 'Master of Public Health')


    )
    SCHEME = (
        ('A-Level certificate', 'A-Level certificate'),
        ('Adult/Mature Learning', 'Adult/Mature Learning',),
        ('Certificate', 'Certificate',),
        ('Diploma', 'Diploma',),
        ('Bachelors', 'Bachelors',),
   
    )

    INTAKE = (
        ('January Intake', 'January Intake',),
        ('May Intake', 'May Intake',),
        ('August Intake', 'August Intake',),
    )

    SPONSOR = (
        ('Private', 'Private', ),
        ('Government', 'Government'),
        ('Bursary', 'Bursary'),
    )
    




    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
         
    ]
    first_name = forms.CharField( required=True , widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="First Name*" )
    last_name = forms.CharField( required=True , widget=forms.widgets.TextInput(attrs={"placeholder":"", "class":"form-control"}), label="Last Name" )
    
    course = forms.ChoiceField(choices=COURSE, required=True, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Select"}),label="Course")
    entry_scheme = forms.ChoiceField(choices=SCHEME, required=True, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Select"}),label="Entry Scheme")
    intake = forms.ChoiceField(choices=INTAKE, required=True, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Select"}),label="Intake")
    sponsor = forms.ChoiceField(choices=SPONSOR, required=True, widget=forms.Select(attrs={"class": "form-control", "placeholder": "Select"}),label="Sponsor")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect(attrs={"class": "form-control", "placeholder": "",}),label="Gender")
    birth_date = forms.CharField( required=True , widget=forms.widgets.TextInput(attrs={"placeholder":" YYYY/MM/DD", "class":"form-control"}), label="Date of Birth",)
    residence = forms.CharField( required=True , widget=forms.widgets.TextInput(attrs={"placeholder":" ", "class":"form-control"}), label="" )
     
    class Meta():
        model = Register
        fields = '__all__'
