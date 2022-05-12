from django.urls import path

from . import views

app_name = 'consulting'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:practice_slug>/', views.detail, name='detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
]