from django.shortcuts import render,redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def index(request):
    return redirect('/shows')

def shows_index(request):
    
    context = {
        'all_shows' : Show.objects.all()
    }
    return render(request , 'shows/index.html' , context)

def new_show(request):
    return render(request,'shows/new.html')

def create_show(request):
    if request.method == 'POST':
        
        errors = Show.objects.show_validations(request.POST)
        
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect('/shows/new')
            
        new_show = Show.objects.create(title = request.POST['title'], network = request.POST['network'] , release_date = request.POST['release_date'], description = request.POST['description'])
        return redirect(f'/shows/{new_show.id}')
    return redirect('shows/new')

def show_detail(request, show_id):
    context = {
        'show' : Show.objects.get(id=show_id)
    }
    return render(request, 'shows/detail.html', context)

def edit_show(request, show_id):
    context = {
        'show': Show.objects.get(id=show_id)
    }
    return render(request, 'shows/edit.html', context)

def update_show(request,show_id):
    if request.method == 'POST':
        
        errors = Show.objects.show_validations(request.POST)
        
        show = Show.objects.get(id=show_id)
        
        if errors:
            for key,value in errors.items():
                messages.error(request,value)
                return redirect(f'/shows/{ show.id }/update')
        
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return redirect(f'/shows/{show_id}')
    return redirect('/shows')

def destroy_show(request,show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows')    
