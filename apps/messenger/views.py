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

from apps.messenger.models import Conversation

# Practices listing view
def index(request):
    conversations = request.user.conversation_set.all().order_by('updated_at') 
    return render(request, 'messenger/index.html', {
        'conversations':conversations
    }) 