from dataclasses import field
from django import forms
from apps.authentication.models import User
from apps.consulting.models import Practice

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'address',
            'city',
            'country',
            'postal',
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                "placeholder": "Nom d'utilisateur",
                "class": "form-control",
            }),

            'email': forms.TextInput(attrs={
                "placeholder": "Email address",
                "class": "form-control"
            }),
            'first_name': forms.TextInput(attrs={
                "placeholder": "Nom",
                "class": "form-control"
            }),
            'last_name': forms.TextInput(attrs={
                "placeholder": "Prénom",
                "class": "form-control"
            }),
            'address': forms.TextInput(attrs={
                "placeholder": "Adresse",
                "class": "form-control"
            }),
            'city': forms.TextInput(attrs={
                "placeholder": "Ville",
                "class": "form-control"
            }),
            'country': forms.TextInput(attrs={
                "placeholder": "Pays",
                "class": "form-control"
            }),
            'postal': forms.TextInput(attrs={
                "placeholder": "Code Postal",
                "class": "form-control"
            }),
        }

class PracticeForm(forms.ModelForm):
    class Meta:
        model = Practice

        fields = [
            'name',
            'address',
            'city',
            'state',
            'zipcode',
            'phone',
            'website',
            'description',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                "placeholder": "Nom du cabinet",
                "class": "form-control",
            }),

            'address': forms.TextInput(attrs={
                "placeholder": "Adresse postale",
                "class": "form-control"
            }),
            'city': forms.TextInput(attrs={
                "placeholder": "Ville",
                "class": "form-control"
            }),
            'state': forms.TextInput(attrs={
                "placeholder": "Département",
                "class": "form-control"
            }),
            'zipcode': forms.TextInput(attrs={
                "placeholder": "Code postal",
                "class": "form-control"
            }),
            'phone': forms.TextInput(attrs={
                "placeholder": "Numéro de téléphone",
                "class": "form-control"
            }),
            'website': forms.TextInput(attrs={
                "placeholder": "Site internet",
                "class": "form-control"
            }),
            'description': forms.Textarea(attrs={
                "placeholder": "Description",
                "class": "form-control rounded-0"
            }),
        }