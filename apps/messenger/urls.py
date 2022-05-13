from django.urls import include, path

from apps.messenger import views

urlpatterns = [
    path('', views.index, name='index'),
]