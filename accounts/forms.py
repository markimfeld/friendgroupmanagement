from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms



class UserAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Usuario...'
            }
        )
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs= {
                'class': 'form-control',
                'placeholder': 'Contraseña...'
            }
        )
    )

