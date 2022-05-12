from django.urls import include, path

from apps.consulting import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:practice_slug>/', views.detail, name='detail'),
]