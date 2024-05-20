from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course =models.CharField(max_length=50)
    entry_scheme = models.CharField(max_length=50)
    intake = models.CharField(max_length=50)
    sponsorship = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    residence = models.CharField(max_length=100)