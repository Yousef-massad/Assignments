from django.shortcuts import render,redirect
from .models import Course
from django.contrib import messages
import bcrypt 

# Create your views here.
def index(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render(request, "courses.html" , context)

def add_course(request):
    if request.method == 'POST':
        
        errors = Course.objects.validate(request.POST)

        if errors:
                for key, value in errors.items():
                    messages.error(request, value)
                return redirect('/')
        
        Course.objects.create(name = request.POST['coursename'], description= request.POST['description'])
        return redirect('/')
        
def remove_id(request, id):
    context = {
        'course': Course.objects.get(id=id) 
    }
    return render(request, 'remove.html', context)

def remove(request,id):
    CourseToRemove = Course.objects.get(id=id)
    CourseToRemove.delete()
    return redirect('/')

