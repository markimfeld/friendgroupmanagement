from django.views.generic.list import ListView
from django.shortcuts import render


# Create your views here.
from .models import (
    Meeting,
    Person
)


class MeetingListView(ListView):
    model = Meeting
    template_name = 'friendgroups/meetings.html'


class PersonListView(ListView):
    model = Person
    template_name = 'friendgroups/members.html'
