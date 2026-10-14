from django.shortcuts import render,redirect
import random

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
        
    return render(request,'index.html')

def process_money(request,location):
    if request.method == 'POST':
        earned_gold = 0
    
    if location == 'farm':
        earned_gold = random.randint(10,20)
        
    elif location == 'cave':
        earned_gold = random.randint(5,10)
        
    elif location == 'house':
        earned_gold = random.randint(2,5)

    elif location == 'quest':
        earned_gold = random.randint(-50,50)
        
    request.session['gold'] += earned_gold
    
    if earned_gold >= 0:
        activity = f"Earned {earned_gold} golds from the {location}! "
        status = 'win'
        
    else:
        activity = f"Entered a quest and lost {abs(earned_gold)} golds... Ouch! "
        status = 'loss'    
        
    request.session['activities'].insert(0, {'text': activity , 'status' : status})
    request.session.modified = True
    
    return redirect('/')

def reset(request):
    request.session.flush()
    return redirect('/')