
from django.shortcuts import render,redirect
from . models import *
from .forms import *
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages

# Create your views here.
def gbt(request):
    if request.method == 'POST' :
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been Successfully submitted')
            return redirect('gbt.html')
        else:
            messages.error(request, 'Failed to add')
    else:
        form = AddForm()
    return render(request,'gbt.html',{'form':form})
