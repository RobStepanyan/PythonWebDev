from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm, UserLogInForm


def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('users-log-in')
    else:
        form = UserSignUpForm()
    context = {
        'form': form, 
        'title': 'Sign Up'
    }
    return render(request, './users/sign_up.html', context)
    

def log_in(request):
    form = UserLogInForm(request.POST)
    context = {
        'form': form, 
        'title': 'Log In'
    }
    return render(request, './users/log_in.html', context)