from django import forms

class PayForm(forms.Form):
    prestation = forms.CharField(label='Your name', max_length=100)