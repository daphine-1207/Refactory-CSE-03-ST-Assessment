from django.shortcuts import render
from .models import Student
# Create your views here.
def Home(request):
    message = False
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        course = request.POST['course']
        entry = request.POST['entry']
        intake = request.POST['intake']
        sponsor = request.POST['sponsorship']
        gender = request.POST['gender']
        dob = request.POST['dob']
        resi = request.POST['residence']
        stud = Student(first_name=fname, last_name=lname, course=course, entry_scheme=entry,  intake=intake, sponsorship=sponsor, gender=gender, date_of_birth=dob, residence=resi)
        stud.save()
        message = True
        return render(request, 'form.html', {'message': message})
    return render(request, 'form.html')