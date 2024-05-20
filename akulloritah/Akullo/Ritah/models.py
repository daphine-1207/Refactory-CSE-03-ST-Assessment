from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
import re


#letter validation
def validate_letters(value):
    if not re.match("^([a-zA-Z]+\s)*[a-zA-Z]+$", value):
        raise ValidationError("Only letters are allowed.")

#number validation function
def validate_numbers(value):
    if not re.match("^[0-9]*$", value):
        raise ValidationError("Only numbers are allowed.")

#contact length validation function
def validate_contact_length(value):
    if len(value) != 10:
        raise ValidationError("Contact field must contain exactly 10 digits.")



# Create your models here.

class Reg(models.Model):
    firstname = models.CharField(max_length=255, blank=False, null=True)
    lastname = models.CharField(max_length=255, blank= False, null=True)  # Removed blank=False constraint
    course = models.CharField(max_length=255, blank=False)
    entry_scheme = models.CharField(max_length=255, blank=False,null=True)
    intake = models.IntegerField(blank=False)
    sponsorship = models.CharField(max_length=255, blank=False)
    gender = models.CharField(max_length=255, blank=False)
    date_of_birth = models.DateField(blank=False)
    residence = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"





