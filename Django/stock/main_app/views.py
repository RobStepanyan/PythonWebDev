from django.shortcuts import render

# Create your views here.
def home(request):
    context = {
        'title': 'Stock Home',
    }
    return render(request, 'main_app/index.html', context)