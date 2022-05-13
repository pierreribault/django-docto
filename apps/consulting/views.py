from datetime import datetime
from decimal import Decimal

from asyncio.log import logger
from logging import Logger
import re
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import get_user_model

import stripe
from apps.consulting import payment

from apps.consulting.models import Billing, Practice, Slot
from apps.consulting.documents import PracticeDocument
from apps.consulting.forms import MessageForm
from apps.consulting.payment import Payment
from apps.messenger.models import Conversation, Message

# Practices listing view
def index(request):
    practice = Practice.objects.all().order_by('id') 
    return render(request, 'practices/index.html', {'practice':practice}) 

def search(request):
    query = request.GET.get('q')
    localisation = request.GET.get('localisation')

    if not query or not localisation:
        return redirect('/')

    practices = PracticeDocument.search().query(
        'multi_match',
        query=query,
        fuzziness='5' # should be changed to improve search results
    )

    return render(request, 'practices/search.html', {
        'query': query,
        'localisation': localisation,
        'practices': practices,
    })

# Practice detail view
# On affiche les services
# On propose un calendar de slot pour lancer le process de réservation
# Un bouton contacter pour avoir le système de messagerie
def detail(request, practice_slug):
    practice = get_object_or_404(Practice, slug=practice_slug)
    services = practice.service_set.all()

    payment = Payment()
    messageForm = MessageForm(request.POST)

    if request.method == 'POST':
        if messageForm.is_valid():
            conversation = Conversation.objects.get_or_create(
                user_one=request.user,
                user_two=practice.user,
            )

            message = Message.objects.create(
                user=request.user,
                conversation=conversation[0],
                message=messageForm.cleaned_data['message'],
            )

            return redirect('messenger_index')
    
    return render(request, 'practices/details.html', {
        'practice': practice,
        'services': services,
        'messageForm': messageForm,
        'stripe_publishable_key': payment.publishableKey(),
    })

def pay(request, practice_slug, service_id):
    practice = get_object_or_404(Practice, slug=practice_slug)
    service = get_object_or_404(practice.service_set, id=service_id)
    slots = practice.slot_set.filter(start_time__gte=datetime.now()).exclude(
        status='paid'
    )

    payment = Payment()

    if request.method == 'POST':
        slot = get_object_or_404(Slot, id=request.POST.get('slot'))
        paymentIntent = payment.createPaymentIntent(service.price, request.POST.get('payment_method_id'))
        paymentIntent = payment.confirmPaymentIntent(paymentIntent.id)
        capture = payment.capture(service.price, paymentIntent.id)

        if capture.status == 'succeeded':
            billing = Billing(
                slot=slot,
                service=service,
                user=request.user,
                transaction_id=paymentIntent.id,
                status='paid'
            )

            billing.save()

            slot.status = 'paid'
            slot.save()
            
            return redirect('/')

    return render(request, 'practices/pay.html', {
        'service': service,
        'practice': practice,
        'slots': slots,
        'stripe_publishable_key': payment.publishableKey(),
    })

def threeDsRedirect(request):
    print('threeds')