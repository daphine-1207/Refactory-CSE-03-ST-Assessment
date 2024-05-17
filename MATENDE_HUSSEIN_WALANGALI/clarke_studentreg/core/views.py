from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import *

# Create your views here.

def studentReg(request):
    if request.method == "POST":
        form = StudentRegForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Form has Been Submitted Successfully!')
            return redirect('/')
        
            # return HttpResponse("You have successfully registered")
        else:
            return HttpResponse("Invalid Form")
    else:
        form = StudentRegForm()

    return render(request, "core/form123.html", {"form": form})


