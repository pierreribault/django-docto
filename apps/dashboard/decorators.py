from functools import wraps
from django.http import HttpResponseRedirect
from apps.authentication.models import User

def rule_practitioner(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        user = request.user
        if user.is_practitioner():
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')

  return wrap

def rule_client(function):
  @wraps(function)
  def wrap(request, *args, **kwargs):

        user = request.user
        if not user.is_practitioner():
             return function(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/')

  return wrap