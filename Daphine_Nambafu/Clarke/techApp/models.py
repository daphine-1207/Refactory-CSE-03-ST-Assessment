from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
import re


# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(3)],  blank=False, null=False)
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(3)], blank=False, null=False)
    COURSE_CHOICES = [
        ('CHS', 'Certificate in Health Science'),
        ('CAT', 'Certicate in Applied Technology'),
        ('BIT', 'Bachelor of Information Technology'),
        ('BBT', 'Bachelor in Business Technology'),
        ('MPH', 'Bachelor of Public Health'),
    ]
    course = models.CharField(max_length=20, choices=COURSE_CHOICES)
  
    ENTRY_SCHEME_CHOICES = [
        ('a level certificate', 'A-Level Certificate'),
        ('learning', 'Adult/Mature Learning'),
        ('certificate', 'Certificate'),
        ('diploma', 'Diploma'),
        ('bachelor', 'BachelorS'),
        
    ]

    entry_scheme = models.CharField(max_length=20, choices=ENTRY_SCHEME_CHOICES )
    SPONSHORSHIP_CHOICES = [
        ('P', 'Private'),
        ('G', 'Government'),
        ('B', 'Bursary'),
    ]
    sponsorship = models.CharField(max_length=20, choices=SPONSHORSHIP_CHOICES)
    INTAKE_CHOICES = [
        ('January', 'January Intake'),
        ('May', 'May Intake'),
        ('August', 'August Intake'),
    ]
    intake = models.CharField(max_length=20, choices=INTAKE_CHOICES)
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    residence = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
