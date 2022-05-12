from django.contrib import admin

from .models import Practice, Service, Slot, Billing

admin.site.register(Practice)
admin.site.register(Service)
admin.site.register(Slot)
admin.site.register(Billing)
