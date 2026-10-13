from django.shortcuts import render,redirect
import random

# Create your views here.
def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1,100)
        request.session['game_status'] = None
        
    return render(request,'index.html')

def guess(request):
    if request.method == 'POST':
        user_guess = int(request.POST.get('guess',0))
        secret_number = request.session['number']
        
        if user_guess > secret_number:
            request.session['game_status'] = 'too_high'
        elif user_guess < secret_number:
            request.session['game_status'] = 'too_low'
        else:
            request.session['game_status'] = 'correct'
            
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')