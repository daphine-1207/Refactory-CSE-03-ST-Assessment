from django.shortcuts import render,redirect
from . models import *
from .forms import *
from django.template import loader
from django.contrib import messages

# Create your views here.

def register(request):
    form = PersonForm(request.POST)
    if request.method == 'POST':
        first_name = request.POST.get('first name')
        last_name = request.POST.get('last name')
        course = request.POST.get('course')
        entry_scheme = request.POST.get('entry_scheme')
        intake = request.POST.get('intake')
        sponsorship = request.POST.get('sponsorship')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date of birth')
        residence = request.POST.get('residence')

        form = Person(first_name=first_name,last_name=last_name,course=course,entry_scheme=entry_scheme,intake=intake,sponsorship=sponsorship,gender=gender,date_of_birth=date_of_birth,residence=residence)
        form.save()
        messages.success(request,'Form has Been Submitted Successfully!')
        return redirect('/')
    else:
        return render(request,'formApp/register.html')

