from django.shortcuts import render, redirect

def index(request):
    
    if 'count' in request.session:
        request.session['count'] += 1
    else:
        request.session['count'] = 1

    # Additional tracking for total site visits
    if 'visits' in request.session:
        request.session['visits'] += 1
    else:
        request.session['visits'] = 1

    return render(request, 'index.html')

def destroy(request):
    if 'count' in request.session:
        del request.session['count']
    if 'visits' in request.session:
        del request.session['visits']
    return redirect('/')

def increment_two(request):
    if 'count' in request.session:
        request.session['count'] += 2
    else:
        request.session['count'] = 2
    return redirect('/')

def custom_increment(request):
    if request.method == 'POST':
        increment_by = int(request.POST.get('increment_value', 1))
        if 'count' in request.session:
            request.session['count'] += increment_by
        else:
            request.session['count'] = increment_by
    return redirect('/')