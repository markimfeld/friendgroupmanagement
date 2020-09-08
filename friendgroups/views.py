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
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import render, reverse, get_object_or_404


# Create your views here.
from .forms import (
    PersonForm,
    MeetingForm,
    AttendanceForm,
    GroupForm
)
from .models import (
    Meeting,
    Person,
    Attendance,
    Group
)



class DashBoardView(TemplateView):
    template_name = 'friendgroups/index.html'


@method_decorator(login_required, name='dispatch')
class GroupListView(ListView):
    model = Group
    template_name = 'friendgroups/groups.html'


@method_decorator(login_required, name='dispatch')
class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'friendgroups/group-add.html'
    success_url = reverse_lazy('friendgroups:groups')


@method_decorator(login_required, name='dispatch')
class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'friendgroups/group-update.html'
    success_url = reverse_lazy('friendgroups:groups')


@method_decorator(login_required, name='dispatch')
class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'friendgroups/group-delete.html'
    success_url = reverse_lazy('friendgroups:groups')


@method_decorator(login_required, name='dispatch')
class MeetingListView(ListView):
    model = Meeting
    template_name = 'friendgroups/meetings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Meeting.objects.filter(group__pk=self.kwargs.get('pk')).all()
        context['group'] = get_object_or_404(Group, pk=self.kwargs.get('pk'))
        return context


class AttendanceInline(InlineFormSetFactory):
    model = Attendance
    form_class = AttendanceForm
    factory_kwargs = {
        'extra': 1,
        'can_delete': True
    }
    formset_kwargs = {'form_kwargs': {'initial': {'group_pk': None}}}

    def get_formset_kwargs(self):
        kwargs = super(AttendanceInline, self).get_formset_kwargs()
        group = get_object_or_404(Group, pk=self.kwargs.get('pk'))
        group_pk = {'group_pk': group.pk}
        kwargs['form_kwargs'].update({'initial': group_pk}) 
        return kwargs


@method_decorator(login_required, name='dispatch')
class MeetingCreateView(PermissionRequiredMixin, CreateWithInlinesView):
    permission_required = 'friendgroups.can_add_meeting'
    model = Meeting
    inlines = [AttendanceInline]
    form_class = MeetingForm
    template_name = 'friendgroups/meeting-add.html'
    group = None

    def get_initial(self):
        self.group = get_object_or_404(Group, pk=self.kwargs.get('pk'))
        return {'group': self.group, }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = get_object_or_404(Group, pk=self.kwargs.get('pk'))
        return context


@method_decorator(login_required, name='dispatch')
class MeetingUpdateView(UpdateWithInlinesView):
    model = Meeting
    inlines = [AttendanceInline]
    form_class = MeetingForm
    template_name = 'friendgroups/meeting-update.html'


    def get_initial(self):
        self.group = get_object_or_404(Group, pk=self.kwargs.get('group_pk'))
        return {'group': self.group, }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group'] = get_object_or_404(Group, pk=self.kwargs.get('group_pk'))
        return context


@method_decorator(login_required, name='dispatch')
class MeetingDetailView(DetailView):
    model = Meeting
    template_name = 'friendgroups/meeting-detail.html'


@method_decorator(login_required, name='dispatch')
class MeetingDeleteView(DeleteView):
    model = Meeting
    template_name = 'friendgroups/meeting-delete.html'

    def get_success_url(self):
        group_pk = self.kwargs.get('group_pk')
        return reverse_lazy('friendgroups:meetings', args=(group_pk, ))


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
