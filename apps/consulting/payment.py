from locale import currency
import stripe
from django.conf import settings

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

    def confirmPaymentIntent(self, paymentIntentId):
        return stripe.PaymentIntent.confirm(paymentIntentId)

    def createPaymentIntent(self, amount, payment_method_id):
        return stripe.PaymentIntent.create(
          amount=amount * 100,
          currency='eur',
          capture_method='manual',
          payment_method=payment_method_id,
          description="Charged from DjANGO-DOCTO",
        )

    def publishableKey(self):
        return settings.STRIPE_PUBLIC_KEY