
from django.shortcuts import render,redirect
from django.http import HttpResponse
from. forms import*
from . models import *
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Form has been submitted successfully")
            return redirect('/')
        else:
            messages.error(request, "Form has errors. Please check your input.")
    else:
        form = Userform()
    
    return render(request, 'index.html', {'form': form})
