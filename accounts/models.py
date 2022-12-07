from django import forms

from contato.models import Contato

# Create your models here.
# from django.db import models


class FormContato(forms.ModelForm):
    class Meta:
        model = Contato
        exclude = ('mostrar', )
