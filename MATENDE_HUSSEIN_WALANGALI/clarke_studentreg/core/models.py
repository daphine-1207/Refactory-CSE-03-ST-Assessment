import re
from django.db import models
from django.forms import ValidationError

# Create your models here.




    
#letter validation
def validate_letters(value):
    if not re.match("^([a-zA-Z]+\s)*[a-zA-Z]+$", value):
        raise ValidationError("Only letters are allowed.")




class StudentReg(models.Model):
    f_name = models.CharField(max_length=50, validators=[validate_letters] )
    l_name = models.CharField( max_length=50, validators=[validate_letters])
    course = models.CharField(max_length=255, choices=(
        ('','-- Select --'),
        ('Certificate in Health Science','certificate in health science'),
        ('Certificate in Applied Technology','certificate in applied technology'),
        ('Bachelor of Information Technology','bachelor of information technology'),
        ('Bachelors in Business Technology','bachelors in business technology'),
        ('Master of Public Health','master of public health'),
    ))
    entry_scheme = models.CharField(max_length=255, choices=(
        ('','-- Select --'),
        ('A-Level Certificate','a-level certificate'),
        ('Adult/Mature Learning','adult/mature learning'),
        ('Certificate','certificate'),
        ('Diploma','diploma'),
        ('Bachelors','bachelors'),
    ))
    intake = models.CharField(max_length=255, choices=(
        ('','-- Select --'),
        ('January Intake','january intake'),
        ('May Intake','may intake'),
        ('August Intake','august intake'),
    ))
    sponsorship = models.CharField(max_length=255, choices=(
        ('','-- Select --'),
        ('Private','private'),
        ('Government','government'),
        ('Bursary','bursary'),
    ))
    gender = models.CharField(max_length=255, choices=(
        ('male','Male'),
        ('female','Female'),
    ))
    dob = models.DateField()
    residence = models.CharField(max_length=255,validators=[validate_letters] )