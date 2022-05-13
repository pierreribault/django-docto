from asyncio.log import logger
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    postal = models.CharField(max_length=255, blank=True)

    def is_practitioner(self):
        return self.practice_set.first() is not None