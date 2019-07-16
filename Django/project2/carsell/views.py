from django.shortcuts import render

def home(request):
    return render(request, 'carsell/base.html', {"title": 'Carsell'})

