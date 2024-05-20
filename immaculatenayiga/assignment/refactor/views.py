from django.shortcuts import render,redirect
from. forms import UserForm
from.models import User
from django.template import loader
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect




def create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added')
            return redirect('create')
        else:
            messages.error(request, 'Failed to add')

    else:
        form = UserForm()
        return render(request, 'drag.html', {'form': form})
     


