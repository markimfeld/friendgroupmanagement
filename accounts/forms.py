from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from friendgroups.models import Group

CHOICES = [(group.id, group.name) for group in Group.objects.all()]

class UserRegisterForm(UserCreationForm):
    group = forms.MultipleChoiceField(
        widget = forms.SelectMultiple(
            attrs = {
                'class': 'form-control' 
            }
        ),
        choices = CHOICES
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'group', 'password1', 'password2', )


    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )

    first_name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    
    last_name = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )
    
    password1 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )

    password2 = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control'
            }
        )
    )


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

