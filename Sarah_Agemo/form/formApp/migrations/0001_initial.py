# Generated by Django 5.0.4 on 2024-05-17 11:07

import django.core.validators
import formApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), formApp.models.validate_letters])),
                ('Last_Name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(3), formApp.models.validate_letters])),
                ('Course', models.CharField(choices=[('Cetificate in Health Science', 'Cetificate in Health Science'), ('Certificate in Applied Technology', 'Certificate in Applied Technology'), ('Bachelor of Information Technology', 'Bachelor of Information Technology'), ('Bachelors in Business Technology', 'Bachelors in Business Technology'), ('Master of Public Health', 'Master of Public Health')], max_length=200)),
                ('Entry_Scheme', models.CharField(choices=[('A-Level certificate', 'A-Level certificate'), ('Adult/Mature Learning', 'Adult/Mature Learning'), ('Certificate', 'Certificate'), ('Diploma', 'Diploma'), ('Bachelors', 'Bachelors')], max_length=50)),
                ('Intake', models.CharField(choices=[('January Intake', 'January Intake'), ('May Intake', 'May Intake'), ('August Intake', 'August Intake')], max_length=50)),
                ('Sponsorship', models.CharField(choices=[('Private', 'Private'), ('Government', 'Government'), ('Bursary', 'Bursary')], max_length=50)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=50)),
                ('Date_Of_Birth', models.DateField(validators=[formApp.models.validate_age])),
                ('Residence', models.CharField(max_length=255, validators=[django.core.validators.MinLengthValidator(2), formApp.models.validate_letters])),
            ],
        ),
    ]