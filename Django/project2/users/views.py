from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm, UserLogInForm


def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('carsell-home')
    else:
        form = UserSignUpForm()
    return render(request, './users/sign_up.html', {'form': form, 'title': 'Sign Up'})
    

def log_in(request):
    form = UserLogInForm(request.POST)
    return render(request, './users/log_in.html', {'form': form, "title": 'Log In'})