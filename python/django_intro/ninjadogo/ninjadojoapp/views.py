from django.shortcuts import render, redirect
from .models import Dojo, Ninja

def index(request):
    context = {
        "all_dojos": Dojo.objects.all()
    }
    return render(request, "index.html", context)

def create_dojo(request):
    if request.method == "POST":
        Dojo.objects.create(
            name=request.POST['name'],
            city=request.POST['city'],
            state=request.POST['state']
        )
    return redirect('/')

def create_ninja(request):
    if request.method == "POST":
        selected_dojo = Dojo.objects.get(id=request.POST['dojo_id'])
        Ninja.objects.create(
            dojo=selected_dojo,
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name']
        )
    return redirect('/')

def delete_dojo(request, dojo_id):
    dojo_to_delete = Dojo.objects.get(id=dojo_id)
    dojo_to_delete.delete()
    return redirect('/')