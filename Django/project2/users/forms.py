from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField(max_length=30, help_text='Required. 30 characters or fewer.')
    first_name = forms.CharField(max_length=30, help_text='Required. 30 characters or fewer.')
    last_name = forms.CharField(max_length=30, help_text='Required. 30 characters or fewer.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserLogInForm(AuthenticationForm):
    pass    