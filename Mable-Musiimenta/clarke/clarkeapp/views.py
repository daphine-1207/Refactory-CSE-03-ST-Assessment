from django.shortcuts import render, redirect
from .forms import IndexForm


def index(request):
    if request.method == 'POST':
        form = IndexForm(request.POST)
        print(form)
     
        if form.is_valid():
            form = IndexForm()
            return render(request, 'index.html', {'form': form, "success": True} )
    else:
        form = IndexForm()
    return render(request, 'index.html', {'form': form, "success": False})

