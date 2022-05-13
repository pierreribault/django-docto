from django.urls import include, path

from apps.consulting import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('<str:practice_slug>/', views.detail, name='detail'),
    path('<str:practice_slug>/pay/<int:service_id>', views.pay, name='pay_service'),
]