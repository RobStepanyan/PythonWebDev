from .models import Post
from .forms import CarSelectForm
from django.shortcuts import render

def home(request):
    form = CarSelectForm(request.POST)
    context = {
        'form': form, 
        'title': 'Carsell',
        'posts': Post.objects.all(),
    }
    return render(request, 'carsell/home.html', context)

def about(request):
    context = {
        'title': 'Our Story',
    }
    return render(request, 'carsell/about.html', context)