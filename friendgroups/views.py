from django.http import HttpResponseRedirect
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, reverse


# Create your views here.
from .models import (
    Meeting,
    Person,
    Attendance
)


class MeetingListView(ListView):
    model = Meeting
    template_name = 'friendgroups/meetings.html'
    queryset = Meeting.objects.all().order_by('-date')


class MeetingDetailView(DetailView):
    model = Meeting
    template_name = 'friendgroups/meeting-detail.html'


class MeetingDeleteView(DeleteView):
    model = Meeting
    template_name = 'friendgroups/meeting-delete.html'

    def get_success_url(self):
        return HttpResponseRedirect(reverse('friendgroups:index'))

class PersonListView(ListView):
    model = Person
    template_name = 'friendgroups/members.html'


