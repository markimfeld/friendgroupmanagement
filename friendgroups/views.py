from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render


# Create your views here.
from .models import (
    Meeting,
    Person,
    Attendance
)


class MeetingListView(ListView):
    model = Meeting
    template_name = 'friendgroups/meetings.html'


class MeetingDetailView(DetailView):
    model = Meeting
    template_name = 'friendgroups/meeting-detail.html'


class PersonListView(ListView):
    model = Person
    template_name = 'friendgroups/members.html'


