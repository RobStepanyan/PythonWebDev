from django.shortcuts import render
from .forms import CarSelectForm

def home(request):
    form = CarSelectForm(request.POST)
    return render(request, 'carsell/home.html', {'form': form, "title": 'Carsell'})

def about(request):
    return render(request, 'carsell/about.html', {'title': 'Our Story'})

