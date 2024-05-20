from django.db import models

# Create your models here.
class Student(models.Model):
     GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
     ]

     COURSE_CHOICES = [
         ('Cetificate in Health Science', 'Cetificate in Health Science'),
         ('Certificate in Applied Technology', 'Certificate in Applied Technology'),
         ('Bachelor of Information Technology', 'Bachelor of Information Technology'),
         ('Bachelors in Business Technology', 'Bachelors in Business Technology'),
         ('Master of Public Health', 'Master of Public Health'),
     ]

     ENTRYSCHEME_CHOICES = [
         ('A-Level certificate', 'A-Level certificate' ),
         ('Adult/Mature Learning', 'Adult/Mature Learning'),
         ('Certificate','Certificate' ),
         ('Diploma','Diploma' ),
         ('Bachelors', 'Bachelors'),
     ]

     INTAKE_CHOICES =[
         ('January Intake', 'January Intake'),
         ('May Intake', 'May Intake'),
         ('August Intake', 'August Intake')
     ]

     SPONSORSHIP_CHOICES =[
         ('Private', 'Private'),
         ('Government', 'Government'),
         ('Bursary', 'Bursary'),
     ]

     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     course = models.CharField(max_length=34, choices=COURSE_CHOICES)
     entryscheme = models.CharField(max_length=21, choices=ENTRYSCHEME_CHOICES)
     intake = models.CharField(max_length=14, choices=INTAKE_CHOICES)
     sponsorship = models.CharField(max_length=10, choices=SPONSORSHIP_CHOICES)
     gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="Male")
     date_of_birth = models.DateField()
     residence = models.CharField(max_length=255)
     


     def __str__(self):
        return f"{self.first_name} {self.last_name}"
    