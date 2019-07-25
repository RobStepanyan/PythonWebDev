from django.shortcuts import render
from .forms import CarSelectForm

def home(request):
    form = CarSelectForm(request.POST)
    context = {
        'form': form, 
        'title': 'Carsell'
    }
    return render(request, 'carsell/home.html', context)

def about(request):
    context = {
        'title': 'Our Story'
    }
    return render(request, 'carsell/about.html', context)

