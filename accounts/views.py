from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as _login, logout as _logout
# from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

# Create your views here.
from .forms import UserAuthenticationForm


def login(request):

    if request.user.is_authenticated:
        return redirect('/')

    form = UserAuthenticationForm()
    
    if request.method == 'POST':
        form = UserAuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                _login(request, user)

                return HttpResponseRedirect(reverse('friendgroups:index'))


    template_name = 'accounts/login.html'

    context = {
        "form": form,
    }
    
    return render(request, template_name, context)


def logout(request):
    if request.user.is_authenticated:
        _logout(request)
        return HttpResponseRedirect(reverse('accounts:login'))
