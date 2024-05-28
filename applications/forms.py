from django import forms
from .models import Student
from django.core.exceptions import ValidationError




entry = [
        ('PhD', 'PhD'),
        ('Masters', 'Masters'),
        ('Degree', 'Degree'),
        ('Certificates', 'Certificates'),
    ]

course = [
        ('ICT', 'ICT'),
        ('Medicine', 'Medicine'),
        ('Nursing', 'Nursing'),
        ('Education', 'Education'),
    ]

intake = [
    ('January intake', 'January intake'),
    ('August intake', 'August intake'),
]

sponsorship = [
    ('Yes', 'Yes'),
    ('No', 'No'),
]

genders = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    
]

class StudentForm(forms.ModelForm):
    first_name = forms.CharField( required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Enter your First Name", "class":"form-control"}), label="First Name" )
    last_name = forms.CharField( required=True , widget=forms.widgets.TextInput(attrs={"placeholder":"Enter your Last Name", "class":"form-control"}), label="Last Name" )
    gender = forms.ChoiceField(required=True, choices=genders, widget=forms.CheckboxInput(attrs={"class": "form-check-input", "placeholder": "Select your Gender"}),label="Gender")
    date_of_birth= forms.CharField( required=True , widget=forms.widgets.TextInput(attrs={"placeholder":"(YY/MM/DD) ", "class":"form-control"}), label="Date Of Birth")
    residence = forms.CharField( required=True , widget=forms.widgets.TextInput(attrs={"placeholder":"Enter your Residence", "class":"form-control"}), label="Residence" )
    intake = forms.ChoiceField(required=True, choices=intake, widget=forms.Select(attrs={"class": "form-control", "placeholder": "choose intake"}),label="Intake")
    course = forms.ChoiceField(required=True, choices=course, widget=forms.Select(attrs={"class": "form-control", "placeholder": "select course"}),label="Course")
    sponsorship = forms.ChoiceField(required=True, choices= sponsorship, widget=forms.Select(attrs={"class": "form-control", "placeholder": "select course"}),label="Sponsorship")
    entry_scheme = forms.ChoiceField(required=True, choices=entry, widget=forms.Select(attrs={"class": "form-control", "placeholder": "select Entry Scheme"}),label="Entry Scheme")

    
    class Meta():
        model = Student
        fields = '__all__'