from django import forms
from.models import User

class UserForm(forms.ModelForm):
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
        ('January Intake', 'January Intake'),
        ('May Intake', 'May Intake'),
        ('August Intake', 'August Intake'),
    )

    SPONSORSHIP_CHOICES = (
        ('Private', 'Private'),
        ('Government', 'Government'),
        ('Bursary', 'Bursary'),
    )

    first_name = forms.CharField(required=True, max_length=100, label="First Name")
    last_name = forms.CharField(required=True, max_length=100, label="Last Name")
    course = forms.ChoiceField(choices=COURSE_CHOICES, required=True, label="Course")
    entry_scheme = forms.ChoiceField(choices=ENTRY_SCHEME_CHOICES, required=True, label="Entry Scheme")
    intake = forms.ChoiceField(choices=INTAKE_CHOICES, required=True, label="Intake")
    sponsorship = forms.ChoiceField(choices=SPONSORSHIP_CHOICES, required=True, label="Sponsorship")
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True, label="Gender")
    date_of_birth = forms.DateField(required=True, label="Date of Birth")

    class Meta:
        model = User
        fields = '__all__'
    
    