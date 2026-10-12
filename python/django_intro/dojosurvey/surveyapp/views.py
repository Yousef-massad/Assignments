from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def result(request):
    
    name_from_form = request.POST["name"]
    location_from_form = request.POST["location"]
    language_from_form = request.POST["language"]
    comment_from_form = request.POST["comment"]
    
    context = {
        'name_on_template' : name_from_form,
        'location_on_template' : location_from_form,
        'language_on_template' : language_from_form,
        'comment_on_template' : comment_from_form,
    }
    
    print(context['comment_on_template'])
    
    return render(request,'result.html',context)
