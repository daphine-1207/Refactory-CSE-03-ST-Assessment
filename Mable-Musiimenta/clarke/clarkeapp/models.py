from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.
class Index(models.Model):
    first_name = models.CharField(max_length=50, validators=[MinLengthValidator(3)], null=False, blank=False)
    last_name = models.CharField(max_length=50, validators=[MinLengthValidator(3)], null=False, blank=False)
    course = models.CharField(max_length=255, null=False, blank=False)
    entry_scheme = models.CharField(max_length=255, null=False, blank=False)
    intake = models.CharField(max_length=255, null=False, blank=False)
    sponsorship = models.CharField(max_length=255, null=False, blank=False)
    gender_choices = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    gender = models.CharField(max_length=50,choices=gender_choices,default="Male", null=False, blank=False)
    date_of_birth = models.DateField(null=False, blank=False)
    residence = models.CharField(max_length=255, null=False, blank=False)

   