
from django.urls import path, re_path
from apps.dashboard import views

urlpatterns = [

    # The dashboard page
    path('', views.index, name='dashboard'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
]
