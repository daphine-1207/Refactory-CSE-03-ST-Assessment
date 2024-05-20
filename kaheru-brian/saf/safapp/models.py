from django.db import models

# Create your models here.
class Student_application(models.Model):
    GENDER_CHOICES ={
        ('Male', 'Male'),
        ('Female', 'Female'),
    }
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    entry_scheme = models.CharField(max_length=100)
    intake = models.CharField(max_length=255)
    sponsorship = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=15, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    residence  = models.CharField(max_length=100)
    
    
