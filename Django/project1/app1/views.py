from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def home(request):
    return render(request, 'app1_templates/home.html', {'title': 'App1 - Home Page', 'posts': Post.objects.all()})

def about(request):
    return render(request, 'app1_templates/about.html', {'title': 'App1 - About Page'})