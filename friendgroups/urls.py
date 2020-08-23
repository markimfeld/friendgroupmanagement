from django.urls import path


from . import views


app_name='friendgroups'
urlpatterns = [
    path('', views.MeetingListView.as_view(),  name='index'),
    path('members', views.PersonListView.as_view(), name='members'),
    path('meetings/<int:pk>/detail/', views.MeetingDetailView.as_view(), name='meeting-detail'),
]
