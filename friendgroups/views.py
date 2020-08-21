from django.views.generic.list import ListView
from django.shortcuts import render


# Create your views here.
from .models import Meeting


class MeetingListView(ListView):
    model = Meeting
