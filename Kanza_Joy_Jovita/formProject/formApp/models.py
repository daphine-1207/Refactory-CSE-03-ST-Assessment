# Create your models here.
from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator,RegexValidator
from django.core.exceptions import ValidationError
import re
from datetime import date
from django.utils.translation import gettext_lazy as _


    
#letter validation
def validate_letters(value):
    if not re.match("^([a-zA-Z]+\s)*[a-zA-Z]+$", value):
        raise ValidationError("Only letters are allowed.")

# #number validation function
# def validate_numbers(value):
#     if not re.match("^[0-9]*$", value):
#         raise ValidationError("Only numbers are allowed.")

# #contact length validation function
# def validate_contact_length(value):
#     if len(value) != 10:
#         raise ValidationError("Contact field must contain exactly 10 digits.")
    


# def validate_age(value):
#     today = date.today()
#     age = today.year - value.year - ((today.month, today.day) < (value.month, value.day))
#     if age < 18:
#         raise ValidationError(_('You must be at least 18 years old.'))

class Person(models.Model):
    first_name = models.CharField(max_length=50, validators=[validate_letters])
    last_name = models.CharField(max_length=50, validators=[validate_letters])
    course = models.CharField(choices=[('Certificate_in_health_science','Certificate_in_health_science'),('Certificate_in_applied_technology','Certificate_in_applied_tecnology'),('Bachelor_in_information_technology','Bachelor_in_information_technology'),('Bachelor_in_business_technology','Bachelor_in_business_technology'),('Masters_in_business_health',('Masters_in_business_health'))],max_length=100, null=False,blank=False)
    entry_scheme =  models.CharField(choices=[('A_level certificate','A_level certificate'),('Adult/mature learning','Adult/mature learning'),('Certificate','Certificate'),('Diploma','Diploma'),('Degree','Degree')],max_length=100, null=False,blank=False)
    intake =  models.CharField(choices=[('January intake','January intake'),('May intake','May intake'),('August intake','August intake')],max_length=100, null=True,blank=False)
    sponsorship = models.CharField(choices=[('Private','Private'),('Government','Government'),('Bursary','Bursary')],max_length=100, null=False,blank=False)
    gender = models.CharField(choices=[('Female','Female'),('Male','Male')],max_length=100,null=False,blank=False)
    date_of_birth = models.DateField(default=timezone.now)
    residence = models.CharField(max_length=255, validators=[validate_letters])

    def __str__(self):
       return f"{self.first_name}{self.last_name}"
    def clean(self):
        # If you want to perform additional model-level validation, you can do it here
        super().clean()

