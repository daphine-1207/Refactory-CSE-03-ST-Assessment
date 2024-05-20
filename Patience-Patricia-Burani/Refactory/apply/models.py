from django.db import models
from django.utils.timezone import datetime
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
import re
# Create your models here.

def validate_letters(value):
    if not re.match("^([a-zA-Z]+\s)*[a-zA-Z]+$", value):
        raise ValidationError("Only letters are allowed.")
# Create your models here.
class Register(models.Model):
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
    first_name = models.CharField( validators=[MinLengthValidator(3),validate_letters], max_length=50, null=True, blank=True)
    last_name = models.CharField( validators=[MinLengthValidator(3),validate_letters], max_length=50, null=True, blank=True)
    

    
    course = models.CharField( max_length=80, choices=COURSE, null=True, blank=True,  )
    entry_scheme = models.CharField(max_length=80 ,choices=SCHEME,  null=True, blank=True,   )
    intake = models.CharField( max_length=80 ,choices=INTAKE, null=True, blank=True, )
    sponsorship = models.CharField( max_length=80, choices=SPONSOR,  null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    residence = models.CharField( validators=[MinLengthValidator(3),validate_letters],  null=True, blank=True, max_length=255)
     
    def __str__(self):
        return f"{self.residence}"
         
        



