from django.urls import path


from . import views


app_name='friendgroups'
urlpatterns = [
    path('', views.DashBoardView.as_view(), name='index'),
    path('groups/', views.GroupListView.as_view(),  name='groups'),
    path('new-group/', views.GroupCreateView.as_view(), name='group-add'),
    path('groups/<int:pk>/update/', views.GroupUpdateView.as_view(), name='group-update'),
    path('groups/<int:pk>/delete/', views.GroupDeleteView.as_view(), name='group-delete'),
    path('groups/<int:pk>/meetings/', views.MeetingListView.as_view(),  name='meetings'),
    path('members/', views.PersonListView.as_view(), name='members'),
    path('new-member/', views.PersonCreateView.as_view(), name='member-add'),
    path('members/<int:pk>/update/', views.PersonUpdateView.as_view(), name='member-update'),
    path('members/<int:pk>/delete/', views.PersonDeleteView.as_view(), name='member-delete'),
    path('meetings/<int:pk>/detail/', views.MeetingDetailView.as_view(), name='meeting-detail'),
    path('groups/<int:group_pk>/meetings/<int:pk>/update/', views.MeetingUpdateView.as_view(), name='meeting-update'),
    path('groups/<int:pk>/meetings/new-meeting/', views.MeetingCreateView.as_view(), name='meeting-add'),
    path('groups/<int:group_pk>/meetings/<int:pk>/delete/', views.MeetingDeleteView.as_view(), name='meeting-delete')
]
