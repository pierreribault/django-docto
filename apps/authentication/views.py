# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from apps.dashboard.forms import PracticeForm
from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


def registerPractitioner(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            if user:
                login(request, user)
                msg = 'User created - please <a href="/login">login</a>.'
                success = True
                return redirect("/createPractice/")
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/registerPractitioner.html", {"form": form, "msg": msg, "success": success})

def createPractice(request):
    form = PracticeForm(request.POST)
    user = request.user
    msg = None
    success = None


    if request.method == "POST":
        form.instance.user = user
        if form.is_valid():
            form.save()
            msg = "Cabinet créée avec succès."
            success = True
        else:
            msg = "Une erreur est survenue lors de la création du cabinet."
            success = False
    return render(request, 'accounts/createPractice.html', {"form": form, "msg": msg, "success": success, "practice": user})