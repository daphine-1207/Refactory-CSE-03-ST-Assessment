from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta


def validate_no_numeric(value):
    if any(char.isdigit() for char in value):
        raise ValidationError('Field should not contain numeric characters')

def validate_age(value):
    today = datetime.now().date()
    age = today - value
    if age.days < 365 * 18:
        raise ValidationError('Age should be at least 18 years old')

def validate_date_of_birth(value):
    today = datetime.now().date()
    if value >= today:
        raise ValidationError('Date of birth cannot be today or a future date.')

class User(models.Model):


    first_name = models.CharField(max_length=100, validators=[validate_no_numeric])
    last_name = models.CharField(max_length=100, validators=[validate_no_numeric])
    course = models.CharField(max_length=100)
    entry_scheme = models.CharField( max_length=100)
    intake = models.CharField( max_length=100)
    sponsorship = models.CharField( max_length=100)
    gender = models.CharField(max_length=10, default='Male')
    date_of_birth = models.DateField(default='YYYY-MM-DD',validators=[validate_date_of_birth, validate_age])
    residence = models.CharField(max_length=255)

    def clean(self):
        super().clean()
        
        if not (3 <= len(self.first_name) <= 50):
            raise ValidationError({'first_name': 'First name should be between 3 and 50 characters long.'})
        
        if not (3 <= len(self.last_name) <= 50):
            raise ValidationError({'last_name': 'Last name should be between 3 and 50 characters long.'})
        
        if not self.course:
            raise ValidationError({'course': 'Course field is required.'})
        
        if not self.entry_scheme:
            raise ValidationError({'entry_scheme': 'Entry scheme field is required.'})
        
        if not self.intake:
            raise ValidationError({'intake': 'Intake field is required.'})
        
        if not self.sponsorship:
            raise ValidationError({'sponsorship': 'Sponsorship field is required.'})
        
        if not (2 <= len(self.residence) <= 255):
            raise ValidationError({'residence': 'Residence should be between 2 and 255 characters long.'})

    def __str__(self):
        return self.first_name
