from django.shortcuts import render,redirect

# Create your views here.
from .models import Student

def student_details(request):
    students = Student.objects.all()
    return render(request, 'student_details.html', {'students': students})



def student_add_show_records(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        roll_number = request.POST.get('roll_number')
        course = request.POST.get('course')
        if name and roll_number and course:
            Student.objects.create(name=name, roll_number=roll_number, course=course)
            return redirect('student-records')  # refresh page

    students = Student.objects.all()
    return render(request, 'student_records.html', {'students': students})