from django.urls import path
from .views import login_view, register_user, registerPractitioner, createPractice
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path('registerPractitioner/', registerPractitioner, name="registerPractitioner"),
    path("createPractice/", createPractice, name="createPractice"),
    path("logout/", LogoutView.as_view(), name="logout")
]
