from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory
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
    MeetingForm
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


class AttendanceInline(InlineFormSetFactory):
    model = Attendance
    fields = ['person', 'is_present']
    factory_kwargs = {
        'extra': 4,
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
