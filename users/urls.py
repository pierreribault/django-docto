from django.urls import include, path
from . import views

app_name = 'users'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('account/', views.profile, name='profile'),
    path('account/', include('django.contrib.auth.urls')),
]