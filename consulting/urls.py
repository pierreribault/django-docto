from django.urls import include, path

from . import views

app_name = 'consulting'
urlpatterns = [
    path('consulting/', views.index, name='index'),
    path('consulting/<str:practice_slug>/', views.detail, name='detail'),
]