from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import datetime, timedelta

class IndexForm(forms.Form):
    first_name = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput())
    last_name = forms.CharField(min_length=3, max_length=50, widget=forms.TextInput())
    courses = [('-- Select --', '-- Select --'), ('Certificate in Health Science', 'Certificate in Health Science'), ('Certificate in Applied technology', 'Certificate in Applied Technology'), ('Bachelor of Information Technology', 'Bachelor of Information Technology'), ('Bachelors in Business Technology', 'Bachelors in Business Technology'), ('Master of Public Health', 'Master of Public Health')]
    course = forms.ChoiceField(choices=courses, widget=forms.Select())
    schemes = [('-- Select--', '-- Select--'), ('A-Level certificate', 'A-Level certificate'), ('Adult/Mature Learning', 'Adult/Mature Learning'), ('Certificate', 'Certificate'), ('Diploma', 'Diploma'), ('Bachelors', 'Bachelors')]
    entry_scheme = forms.ChoiceField(choices=schemes, widget=forms.Select())
    intakes = [('-- Select--', '-- Select--'), ('January Intake', 'January Intake'), ('May Intake', 'May Intake'), ('August Intake', 'August Intake')]
    intake = forms.ChoiceField(choices=intakes, widget=forms.Select())
    sponsorships = [('-- Select --', '-- Select --'), ('Private', 'Private'), ('Government', 'Government'), ('Bursary', 'Bursary')]
    sponsorship = forms.ChoiceField(choices=sponsorships, widget=forms.Select())

    gender_choices = [('Male', 'Male'), ('Female', 'Female')]

    gender = forms.ChoiceField(choices=gender_choices, widget=forms.RadioSelect(attrs={ 'default': 'Male'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'YYYY/MM/DD'}))
    residence = forms.CharField(min_length=3, max_length=255, widget=forms.TextInput())

    
   
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if any(char.isdigit() for char in first_name):
            raise ValidationError("First name should not contain numeric characters.")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if any(char.isdigit() for char in last_name):
            raise ValidationError("Last name should not contain numeric characters.")
        return last_name
    
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get('date_of_birth')
        if date_of_birth:
            if date_of_birth >= timezone.now().date():
                raise ValidationError("Date of birth should be in the past.")
            age = timezone.now().date().year - date_of_birth.year - ((timezone.now().date().month, timezone.now().date().day) < (date_of_birth.month, date_of_birth.day))
            if age < 18:
                raise ValidationError("You must be at least 18 years old to register.")
        return date_of_birth


    def clean_gender(self):
        gender = self.cleaned_data['gender']
        if gender == '-- Select Gender --':
            raise ValidationError("Please select a valid gender.")
        return gender
