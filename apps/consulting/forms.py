from django import forms

class PayForm(forms.Form):
    prestation = forms.CharField(label='Your name', max_length=100)

class MessageForm(forms.Form):
    message = forms.CharField(label='Your message', max_length=100)