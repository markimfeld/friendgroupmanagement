from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, reverse


# Create your views here.
from .forms import (
    PersonForm
)
from .models import (
    Meeting,
    Person,
    Attendance
)


@method_decorator(login_required, name='dispatch')
class MeetingListView(ListView):
    model = Meeting
    template_name = 'friendgroups/meetings.html'
    queryset = Meeting.objects.all().order_by('-date')


@method_decorator(login_required, name='dispatch')
class MeetingDetailView(DetailView):
    model = Meeting
    template_name = 'friendgroups/meeting-detail.html'


@method_decorator(login_required, name='dispatch')
class MeetingDeleteView(DeleteView):
    model = Meeting
    template_name = 'friendgroups/meeting-delete.html'
    success_url = reverse_lazy('friendgroups:index')


@method_decorator(login_required, name='dispatch')
class PersonListView(ListView):
    model = Person
    template_name = 'friendgroups/members.html'


@method_decorator(login_required, name='dispatch')
class PersonCreateView(CreateView):
    model = Person
    template_name = 'friendgroups/member-add.html'
    form_class = PersonForm
    success_url = reverse_lazy('friendgroups:members')


@method_decorator(login_required, name='dispatch')
class PersonUpdateView(UpdateView):
    model = Person
    template_name = 'friendgroups/member-edit.html'
    form_class = PersonForm
    success_url = reverse_lazy('friendgroups:members')


@method_decorator(login_required, name='dispatch')
class PersonDeleteView(DeleteView):
    model = Person
    template_name = 'friendgroups/member-delete.html'
    success_url = reverse_lazy('friendgroups:members')
