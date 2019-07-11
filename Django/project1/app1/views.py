from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>This is a fuckin home page of app1</h1>')

def about(request):
    return HttpResponse('<h1>And this is its fuckin brother about page</h1>')
