from django import forms


from .models import Person, Meeting, Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        labels = { 
            'name': 'Nombre',
            'address': 'Direccion',
            'neighborhood': 'Barrio'
        }


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

    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)

        initial = kwargs.get('initial')

        self.fields['group'].queryset = Group.objects.filter(pk=initial.get('group').id)



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


class AttendanceForm(forms.ModelForm):
    class Meta:
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)

