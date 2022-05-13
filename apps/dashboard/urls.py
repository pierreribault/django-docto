
from django.urls import path, re_path
from apps.dashboard import views

urlpatterns = [

    # The dashboard page
    path('', views.index, name='dashboard'),

    path('profile', views.profile, name='profile'),
    path('practice', views.practice, name='practice'),
    path('slot', views.slot, name='slot'),
    path('slot/new', views.slot_new, name='slot_new'),
    path('slot/<int:slot_id>/delete', views.slot_delete, name='slot_delete'),
    path('service', views.service, name='service'),
    path('service/new', views.service_new, name='service_new'),
    path('service/<int:service_id>/delete', views.service_delete, name='service_delete'),
    path('calendar', views.calendar, name='calendar'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
