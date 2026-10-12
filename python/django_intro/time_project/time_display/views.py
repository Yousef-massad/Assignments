from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
    now = datetime.now()
    context = {
        "date": now.strftime("%b %d %Y"),
        "time": now.strftime("%I %M %p")
    }
    return render(request, 'index.html', context)
