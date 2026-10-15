from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
  users = User.objects.all()
  context = {
      'users': users,
    }
  return render(request, 'index.html' , context)

def add(request):
  if request.method == 'POST':
    User.objects.create(
    first_name=request.POST['first_name'], 
    last_name=request.POST['last_name'], 
    email=request.POST['email'], 
    age=request.POST['age']
    )
  return redirect('/')

def remove(request, id):
  if request.method == 'POST':
    user_id = User.objects.get(id=id)
    user_id.delete()
  return redirect('/')

def update(request, id):
  user_id = User.objects.get(id=id)
  if request.method == 'POST':
    user_id.first_name=request.POST['first_name']
    user_id.last_name=request.POST['last_name']
    user_id.email=request.POST['email']
    user_id.age=request.POST['age']
    user_id.save()
    return redirect('/')

  return render(request, 'update.html', {'user': user_id})