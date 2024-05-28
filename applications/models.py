from django.db import models
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

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=200, blank=False)
    last_name = models.CharField(max_length=200, blank=False, null=True)
    course = models.CharField(max_length=200, choices=course)
    entry_Scheme = models.CharField(max_length=200, choices=entry, blank=False, null=True)
    intake = models.CharField(max_length=200,blank=False, null=True)
    sponsorship = models.CharField(max_length=200, blank=False, null=True)
    gender = models.CharField(max_length=200, blank=True, null=True)
    date_of_birth = models.DateField()
    residence = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name + " " + self.last_name
    



