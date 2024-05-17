from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentApplicationForm

def application(request):
    if request.method == 'POST':
        form = StudentApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form has been submitted successfully.')
            return redirect('application')  # Redirect to the same view to clear the form
    else:
        form = StudentApplicationForm()
    
    return render(request, 'application.html', {'form': form})
