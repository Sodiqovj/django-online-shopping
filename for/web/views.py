from django.shortcuts import render
from .models import *

def home(request):
    home = Car.objects.all()
    context = {
        "source":home
    }
    return render(request, 'index.html', context)
