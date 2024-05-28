from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages

# Create your views here.

def homePage(request):
    return render(request, 'applications/home.html')
    

def register(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student Registered Successfully')
            return redirect('/')  
        else:
            messages.error(request, 'Student Registration Failed')
    else:
        form = StudentForm()

    return render(request, 'applications/register.html', {'form': form})





