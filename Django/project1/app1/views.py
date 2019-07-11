from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {
        "author": "Robert",
        "title": "First post",
        "content": "First post's content",
        "date_posted": "11-Jul-2019"
    },
    {
        "author": "John",
        "title": "Second post",
        "content": "Second post's content",
        "date_posted": "11-Jul-2019"
    },
]


def home(request):
    return render(request, 'app1_templates/home.html', {'title': 'App1 - Home Page', 'posts': posts})

def about(request):
    return render(request, 'app1_templates/about.html', {'title': 'App1 - About Page'})