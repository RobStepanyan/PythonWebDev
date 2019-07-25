"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('carsell.urls')),
    
    path('signup/', user_views.sign_up, name="users-sign-up"),
    path('login/', auth_views.LoginView.as_view(template_name='users/log_in.html'), name='users-log-in'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/log_out.html'), name='users-log-out'),
    path('profile/', user_views.profile, name='users-profile')
]
