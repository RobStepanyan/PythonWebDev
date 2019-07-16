from django.shortcuts import render

def home(request):
    return render(request, 'carsell/home.html', {"title": 'Carsell'})

