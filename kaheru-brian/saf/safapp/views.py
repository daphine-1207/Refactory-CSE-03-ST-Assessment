from django.shortcuts import render
from.models import Student_application
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        course = request.POST.get('course')
        entry_scheme = request.POST.get('entry_scheme')
        intake = request.POST.get('intake')
        sponsorship = request.POST.get('sponsorship')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('date_of_birth')
        residence = request.POST.get('residence')
        
        form_instance  = Student_application(
            first_name = first_name,
            last_name = last_name,
            course = course,
            entry_scheme = entry_scheme,
            intake = intake,
            sponsorship = sponsorship,
            gender = gender,
            date_of_birth = date_of_birth,
            residence = residence,
        )
        form_instance.save()
        messages.success(request, 'Your form has been successsfully submitted')
        return render(request,'safapp/index.html')
    else:
        return render(request,'safapp/index.html')
    
