from django import forms
from .models import Contact


class CreateModel(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'subject',
            'pengirim',
            'email',
            'deskripsi',
        ]
