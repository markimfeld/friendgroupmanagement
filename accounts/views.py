from django.contrib.auth import authenticate, login as _login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.


def login(request):
    form = AuthenticationForm()
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                _login(request, user)

                return redirect('/')


    template_name = 'accounts/base.html'

    context = {
        "form": form,
    }
    
    return render(request, template_name, context)
