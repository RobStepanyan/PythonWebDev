from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import UserSignUpForm

def sign_up(request):
    form = UserSignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'Account created for {username}')
        return redirect('home')
    else:
        form = UserSignUpForm()
        context = {
            'title': 'Sign Up',
            'form': UserSignUpForm,
        }
        return render(request, 'users/sign_up.html', context)
    