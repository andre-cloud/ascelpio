from django.shortcuts import render
from .models import *

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html', {'materie': materie})

def contact(request):
    return render(request, 'contact.html')