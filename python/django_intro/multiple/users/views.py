from django.http import HttpResponse

def register(request):
    return HttpResponse("placeholder for users to create a new user record.")

def login(request):
    return HttpResponse("placeholder for users to log in.")

def index(request):
    return HttpResponse("placeholder to display all the list of users later.")