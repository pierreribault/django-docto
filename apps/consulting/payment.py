from locale import currency
import stripe
from django.conf import settings

from apps.consulting.models import Billing

class Payment():
    apiKey = ''

    def __init__(self):
        self.apiKey = settings.STRIPE_SECRET_KEY
        stripe.api_key = self.apiKey

    def capture(self, amount, payment_intent_id):
        return stripe.PaymentIntent.capture(
          payment_intent_id,
          amount=amount * 100,
        )

    def confirm_payment_intent(self, paymentIntentId):
        return stripe.PaymentIntent.confirm(paymentIntentId)

    def create_payment_intent(self, amount, payment_method_id):
        return stripe.PaymentIntent.create(
          amount=amount * 100,
          currency='eur',
          capture_method='manual',
          payment_method=payment_method_id,
          description="Charged from DjANGO-DOCTO",
        )

    def handle_successful_payment(self, capture, service, slot, user):
        billing = Billing()
        billing.service = service
        billing.slot = slot
        billing.user = user
        billing.status = capture.status
        billing.transaction_id = capture.id
        billing.save()

        return billing


    def publishable_key(self):
        return settings.STRIPE_PUBLIC_KEY