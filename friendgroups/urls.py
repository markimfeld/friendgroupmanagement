from django.urls import path


from . import views


app_name='friendgroups'
urlpatterns = [
    path('', views.MeetingListView.as_view(),  name='index'),
    path('members', views.PersonListView.as_view(), name='members'),
    path('new-member/', views.PersonCreateView.as_view(), name='member-add'),
    path('members/<int:pk>/update/', views.PersonUpdateView.as_view(), name='member-update'),
    path('members/<int:pk>/delete/', views.PersonDeleteView.as_view(), name='member-delete'),
    path('meetings/<int:pk>/detail/', views.MeetingDetailView.as_view(), name='meeting-detail'),
    path('new-meeting/', views.MeetingCreateView.as_view(), name='meeting-add'),
    path('meetings/<int:pk>/delete/', views.MeetingDeleteView.as_view(), name='meeting-delete')
]
