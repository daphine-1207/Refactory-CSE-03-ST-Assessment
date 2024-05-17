from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
import re
from datetime import date
from django.utils.translation import gettext_lazy as _
# Create your models here.

def validate_letters(value):
    if not re.match("^([a-zA-Z]+\s)*[a-zA-Z]+$", value):
        raise ValidationError("Only letters are allowed.")
    
def validate_age(value):
    today = date.today()
    age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
    if age < 18:
        raise ValidationError(_('You must be at least 18 years old.'))

class User(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    
    COURSE=(('Certificate in Health Science', 'Certificate in Health Science'),('Certificate in Applied Technology', 'Certificate in Applied Technology'),('Bachelor of  Information Technology', 'Bachelor of Information Technology'),('Bachelors in Business Technology', 'Bachelors in Business Technology'),('Master of Public Health', 'Master of Public '))
    PERSON=(('January Intake', 'January Intake'),('May Intake', 'May Intake'),('August Intake','August Intake'),)
    COMERS=(('Private', 'Private'),('Government', 'Government'),('Bursary','Bursary'),)    

    Firstname = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    Lastname = models.CharField(validators=[MinLengthValidator(3)], max_length=50)
    Course = models.CharField(choices=COURSE , max_length=50)
    Entry_Scheme = models.CharField(max_length=255, choices= [('A_Level certificate', 'A_Level certificate'),('Adult/Ma',' Adult/Mature Learning'),('Certificate', 'Certificate'),('Diploma', 'Diploma'),('Bachelors', 'Bachelors')])
    Intake=models.CharField(choices=PERSON, max_length=255)
    Sponsorship = models.CharField(max_length=255, choices=COMERS)
    Gender = models.CharField(choices=GENDER, max_length=255)
    Date_of_Birth = models.DateField(validators=[validate_age])
    Residence = models.CharField(validators=[MinLengthValidator(2)], max_length=255)
    def __str__(self):
        return self.firstname + " " + self.lastname
    
    def clean(self):
        # If you want to perform additional model-level validation, you can do it here
        super().clean()