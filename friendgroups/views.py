from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import (
    login_required, 
    permission_required
)
from extra_views import (
    CreateWithInlinesView, 
    UpdateWithInlinesView, 
    InlineFormSetFactory
)
from django import forms
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
    PersonForm,
    MeetingForm,
    AttendanceForm
)
from .models import (
    Meeting,
    Person,
    Attendance,
    Group
)

from django.utils.datastructures import MultiValueDict


@method_decorator(login_required, name='dispatch')
class GroupListView(ListView):
    model = Group
    template_name = 'friendgroups/groups.html'


@method_decorator(login_required, name='dispatch')
class MeetingListView(ListView):
    model = Meeting
    template_name = 'friendgroups/meetings.html'
    queryset = Meeting.objects.all().order_by('-date')


class AttendanceInline(InlineFormSetFactory):
    model = Attendance
    form_class = AttendanceForm
    factory_kwargs = {
        'extra': 1,
        'can_delete': True
    }

    

@method_decorator(login_required, name='dispatch')
class MeetingCreateView(PermissionRequiredMixin, CreateWithInlinesView):
    permission_required = 'friendgroups.can_add_meeting'
    model = Meeting
    inlines = [AttendanceInline]
    form_class = MeetingForm
    template_name = 'friendgroups/meeting-add.html'
    success_url = reverse_lazy('friendgroups:index')


@method_decorator(login_required, name='dispatch')
class MeetingUpdateView(UpdateWithInlinesView):
    model = Meeting
    inlines = [AttendanceInline]
    form_class = MeetingForm
    template_name = 'friendgroups/meeting-update.html'
    success_url = reverse_lazy('friendgroups:index')


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
class PersonCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'friendgroups.can_add_person'
    model = Person
    template_name = 'friendgroups/member-add.html'
    form_class = PersonForm
    success_url = reverse_lazy('friendgroups:members')


@method_decorator(login_required, name='dispatch')
class PersonUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'friendgroups.can_edit_person'
    model = Person
    template_name = 'friendgroups/member-edit.html'
    form_class = PersonForm
    success_url = reverse_lazy('friendgroups:members')


@method_decorator(login_required, name='dispatch')
class PersonDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'friendgroups.can_delete_person'
    model = Person
    template_name = 'friendgroups/member-delete.html'
    success_url = reverse_lazy('friendgroups:members')
