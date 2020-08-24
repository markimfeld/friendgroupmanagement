from django import forms


from .models import Person


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'phone': forms.NumberInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'group': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'category': forms.Select(
                attrs = {
                    'class': 'form-control'
                }
            ),
        }
