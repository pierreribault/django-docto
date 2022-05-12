from django import forms
from apps.authentication.models import User

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