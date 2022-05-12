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
