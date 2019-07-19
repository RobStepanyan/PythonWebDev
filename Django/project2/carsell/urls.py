from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='carsell-home'),
    path('about/', views.about, name='carsell-about'),
]