from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UserSignUpForm


def sign_up(request):
    form = UserSignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(
            request, f'Account created for {username}, now you are able to log in')
        return redirect('log_in')
    else:
        form = UserSignUpForm()
        context = {
            'title': 'Sign Up',
            'form': UserSignUpForm,
        }
        return render(request, 'users/sign_up.html', context)


@login_required
def profile(request):
    context = {
        'title': 'Profile',
    }
    return render(request, 'users/profile.html', context)
