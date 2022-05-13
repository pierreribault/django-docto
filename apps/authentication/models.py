from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    CLIENT = 1
    PRACTITIONER = 2
     
    ROLE_CHOICES = (
        (CLIENT, 'Client'),
        (PRACTITIONER, 'Practitioner'),
    )

    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=False, default=CLIENT)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    postal = models.CharField(max_length=255, blank=True)

    def is_practitioner(self):
        return self.role == self.PRACTITIONER
