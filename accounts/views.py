from django.contrib.auth.models import User
from django.utils.http import (
    urlsafe_base64_encode,url_has_allowed_host_and_scheme, urlsafe_base64_decode,
)
from django.utils.translation import gettext_lazy as _
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'アクティベートする必要があります'
            message = render_to_string('registration/email_body.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('accounts:activation_request')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def activation_request(request):
    return render(request, 'registration/activation_request.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('accounts:login')
    else:
        return render(request, 'registration/activated.html')
