from django import forms


from .models import Person, Meeting


class MeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = '__all__'
        exclude = ('person',)

        widgets = {
            'date': forms.DateInput(
                attrs = {
                    'class': 'form-control datetimepicker-input',
                    'data-target': '#reservationdate'
                }
            ),
            'hour': forms.TimeInput(
                attrs = {
                    'class': 'form-control datetimepicker-input',
                    'data-target': '#timepicker'
                }
            ),
            'topic': forms.TextInput(
                attrs = {
                    'class': 'form-control'
                }
            ),
            'offering': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'min': 0
                }
            ),
            'tithe': forms.NumberInput(
                attrs = {
                    'class': 'form-control',
                    'min': 0
                }
            ),
            'group': forms.Select(
                attrs = {
                    'class': 'form-control select2bs4'
                }
            )
        }

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
