
from asyncio.log import logger
from datetime import datetime, timedelta
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.urls import reverse
from django.core.paginator import Paginator
from apps.dashboard.decorators import rule_practitioner
from django.db.models import Count
from apps.consulting.models import Billing

from apps.dashboard.forms import PracticeForm, ProfileForm, ServiceForm, SlotForm


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('dashboard/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def profile(request):
    form = ProfileForm(request.POST or None, instance=request.user)

    msg = None
    success = None

    if request.method == "POST":
        if form.is_valid():
            form.save()
            msg = "Profil mis à jour avec succès."
            success = True
        else:
            msg = "Une erreur est survenue lors de la modification du profil."
            success = False

    return render(request, "dashboard/profile.html", {"form": form, "msg": msg, "success": success})


@login_required(login_url="/login/")
@rule_practitioner
def practice(request):
    form = PracticeForm(request.POST or None,
                        instance=request.user.practice_set.first())

    msg = None
    success = None

    if request.method == "POST":
        if form.is_valid():
            form.save()
            msg = "Cabinet mis à jour avec succès."
            success = True
        else:
            msg = "Une erreur est survenue lors de la modification du cabinet."
            success = False

    return render(request, "dashboard/practice.html", {"form": form, "msg": msg, "success": success})


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
@rule_practitioner
def slot(request):
    slots_list = request.user.practice_set.first().slot_set.all().order_by('start_time')
    paginator = Paginator(slots_list, 10)
    page = request.GET.get('page')

    if request.GET.get('delete') == 'true':
        msg = "Créneau supprimé avec succès."
    else:
        msg = None

    slots = paginator.get_page(page)

    return render(request, "dashboard/slot.html", {"slots": slots, "msg": msg})


@login_required(login_url="/login/")
@rule_practitioner
def slot_new(request):
    form = SlotForm(request.POST or None)
    practice = request.user.practice_set.first()
    msg = None
    success = None

    if request.method == "POST":
        form.instance.practice_id = practice.id

        if form.is_valid() and form.instance.start_time < form.instance.end_time:
            form.save()
            msg = "Créneau ajouté correctement"
            success = True
        else:
            msg = "Une erreur est survenue lors de l'ajout du créneau, assurez-vous que les dates sont correctes"
            success = False

    return render(request, "dashboard/new-slot.html", {"form": form, "msg": msg, "success": success, "practice": practice})


@login_required(login_url="/login/")
def slot_delete(request, slot_id):
    slot = request.user.practice_set.first().slot_set.get(id=slot_id)
    slot.delete()

    return redirect('/dashboard/slot?delete=true')


@login_required(login_url="/login/")
@rule_practitioner
def service(request):
    service_list = request.user.practice_set.first().service_set.all().order_by('name')
    paginator = Paginator(service_list, 10)
    page = request.GET.get('page')

    if request.GET.get('delete') == 'true':
        msg = "Service supprimé avec succès."
    else:
        msg = None

    services = paginator.get_page(page)

    return render(request, "dashboard/service.html", {"services": services, "msg": msg})


@login_required(login_url="/login/")
def service_new(request):
    form = ServiceForm(request.POST or None)
    practice = request.user.practice_set.first()
    msg = None
    success = None

    if request.method == "POST":
        form.instance.practice_id = practice.id

        if form.is_valid():
            form.save()
            msg = "Service ajouté correctement"
            success = True
        else:
            msg = "Une erreur est survenue lors de l'ajout du service"
            success = False

    return render(request, "dashboard/new-service.html", {"form": form, "msg": msg, "success": success, "practice": practice})


@login_required(login_url="/login/")
def service_delete(request, service_id):
    service = request.user.practice_set.first().service_set.get(id=service_id)
    service.delete()

    return redirect('/dashboard/service?delete=true')

@login_required(login_url="/login/")
def calendar(request):

    page = request.GET.get('page') or ""
    if not page.isdigit() or int(page) < 1:
        page = 1

    monday = datetime.today() - timedelta(days=datetime.today().weekday()) + timedelta(days=(int(page)-1)*7)
    tuesday = monday + timedelta(days=1)
    wednesday = monday + timedelta(days=2)
    thursday = monday + timedelta(days=3)
    friday = monday + timedelta(days=4)
    saturday = monday + timedelta(days=5)

    billings_monday = Billing.objects.filter(slot__start_time__date=monday).order_by('slot__start_time')
    billings_tuesday = Billing.objects.filter(slot__start_time__date=tuesday).order_by('slot__start_time')
    billings_wednesday = Billing.objects.filter(slot__start_time__date=wednesday).order_by('slot__start_time')
    billings_thursday = Billing.objects.filter(slot__start_time__date=thursday).order_by('slot__start_time')
    billings_friday = Billing.objects.filter(slot__start_time__date=friday).order_by('slot__start_time')
    billings_saturday = Billing.objects.filter(slot__start_time__date=saturday).order_by('slot__start_time')

    days = Billing.objects.values('slot__start_time__date').annotate(count=Count('slot__id')).values('slot__start_time', 'slot__end_time', 'count').order_by('slot__start_time__date')

    return render(request, "dashboard/calendar.html", {"days": days, "billings_monday": billings_monday, "billings_tuesday": billings_tuesday, "billings_wednesday": billings_wednesday, "billings_thursday": billings_thursday, "billings_friday": billings_friday, "billings_saturday": billings_saturday, "monday": monday, "saturday": saturday})