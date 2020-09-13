from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as _login, logout as _logout
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse

# Create your views here.
from .forms import UserAuthenticationForm, UserRegisterForm

from friendgroups.models import Group


def new_user(request):
    form = UserRegisterForm()
    
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            user.refresh_from_db() # load the profile instance created by the signal
            groups_list = form.cleaned_data['group']
            groups_list = [int(g) for g in groups_list]

            groups = []
            
            for group in Group.objects.all():
                for g in groups_list:
                    if g == group.id:
                        groups.append(group)

            user.profile.group.set(groups)
            user.save()
            
            return HttpResponseRedirect(reverse('friendgroups:leaders'))
    
    template_name = 'accounts/user-add.html'
    context = {
        "form": form
    }

    return render(request, template_name, context)


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
