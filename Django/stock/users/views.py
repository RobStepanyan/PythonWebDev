from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import login
from stock import settings
import smtplib, os

from .forms import UserCreationFormModified
from .token_generator import account_activation_token


def sign_up(request):
    if request.method == 'POST':
        form = UserCreationFormModified(request.POST)
        if form.is_valid():
            user = form.save()
            smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
            smtpserver.ehlo()
            smtpserver.starttls()
            smtpserver.ehlo()
            smtpserver.login('stockinfonoreply@gmail.com', '48155216')
            smtpserver.sendmail(from_addr='stockinfonoreply@gmail.com', to_addrs='csgobestone@gmail.com', msg='Hiiii', )
            return render(request, './users/check_email.html')
    else:
        form = UserCreationFormModified()
        context = {
            'title': 'Sign Up',
            'form': form,
        }
        return render(request, './users/sign_up.html', context)

def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('./users/account_activated.html')
    else:
        return redirect('./users/activation_link_invalid.html')