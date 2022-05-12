
from asyncio.log import logger
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.core.paginator import Paginator

from apps.dashboard.forms import PracticeForm, ProfileForm, SlotForm


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('dashboard/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def profile(request):
    form = ProfileForm(instance=request.user)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            form.save()
            msg = "oui c'est bon"
        else:
            logger.error(form.errors.as_text())
            logger.error(form.non_field_errors().as_text())
            msg = "test"

    return render(request, "dashboard/profile.html", {"form": form, "msg": msg})

@login_required(login_url="/login/")
def practice(request):
    form = PracticeForm(instance=request.user)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            form.save()
            msg = "oui c'est bon x2"
        else:
            logger.error(form.errors.as_text())
            logger.error(form.non_field_errors().as_text())
            msg = "test x2"

    return render(request, "dashboard/practice.html", {"form": form, "msg": msg})

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('dashboard/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('dashboard/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('dashboard/page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def slot(request):
    slots_list = request.user.practice_set.first().slot_set.all()
    paginator = Paginator(slots_list, 10)
    page = request.GET.get('page')
    slots = paginator.get_page(page)

    return render(request, "dashboard/slot.html", {"slots": slots})

@login_required(login_url="/login/")
def slot_new(request):
    form = SlotForm(request.POST or None)

    msg = None
    success = None

    practice = request.user.practice_set.first()

    if request.method == "POST":
        form.instance.practice_id = practice.id

        if form.is_valid():
            form.save()
            msg = "Créneau ajouté correctement"
            success = True
        else:
            msg = "Une erreur est survenue lors de l'ajout du créneau"
            success = False

    return render(request, "dashboard/new-slot.html", {"form": form, "msg": msg, "success": success, "practice": practice})