from django.shortcuts import render,redirect
from . models import *
from .forms import *
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('first name')
        last_name = request.POST.get('last name')
        course = request.POST.get('course')
        entry_scheme = request.POST.get('entry scheme')
        sponsorship = request.POST.get('sponsorship')
        intake = request.POST.get('intake')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date of birth')
        residence = request.POST.get('residence')
        form = Student(first_name=first_name,last_name=last_name,course=course,entry_scheme=entry_scheme,sponsorship=sponsorship,intake=intake,gender=gender,date_of_birth=date_of_birth,residence=residence)
        form.save()
        messages.success(request,'Form has Been Submitted Successfully!')
        return redirect('/')
    else:
        return render(request,'techApp/index.html')
