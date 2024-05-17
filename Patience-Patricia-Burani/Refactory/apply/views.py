from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .models import Register   
from .forms import RegisterForm  

def add_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been submitted successfully! ')
            return redirect('add_register')   
    else:
        form = RegisterForm()

    return render(request, 'add_register.html', {'form': form})

 


