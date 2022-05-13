from django.db import models
from django.utils.text import slugify
from apps.authentication.models import User

import uuid

class Conversation(models.Model):
    user_one = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_one")
    user_two = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_two")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
