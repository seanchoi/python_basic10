from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import uuid

# Create your views here.

def index(request):
    return render(request, 'generator/index.html')

def wordGenerator(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    request.session['random'] = get_random_string(length=14)
    return render(request, 'generator/index.html')

def reset(request):
    request.session.flush()
    return redirect('/')

