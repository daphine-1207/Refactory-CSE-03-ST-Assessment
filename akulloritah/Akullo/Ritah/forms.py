from django import forms
from .models import Reg

class Form(forms.ModelForm):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    COURSE_CHOICES = (
        ('Certificate in Health Science', 'Certificate in Health Science'),
        ('Certificate in Applied Technology', 'Certificate in Applied Technology'),
        ('Bachelor of Information Technology', 'Bachelor of Information Technology'),
        ('Bachelors in Business Technology', 'Bachelors in Business Technology'),
        ('Master of Public Health', 'Master of Public Health'),
    )

    ENTRY_SCHEME_CHOICES = (
        ('A-Level certificate', 'A-Level certificate'),
        ('Adult/Mature Learning', 'Adult/Mature Learning'),
        ('Certificate', 'Certificate'),
        ('Diploma', 'Diploma'),
        ('Bachelors', 'Bachelors'),
    )

    INTAKE_CHOICES = (
        (1, 'January Intake'),
        (2, 'May Intake'),
        (3, 'August Intake'),
    )

    SPONSORSHIP_CHOICES = (
        ('Private', 'Private'),
        ('Government', 'Government'),
        ('Bursary', 'Bursary'),
    )
class AddForm(forms.ModelForm):
    class Meta:
        model = Reg
        fields = '__all__'
