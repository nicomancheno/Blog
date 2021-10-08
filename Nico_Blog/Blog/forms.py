from django.forms import ModelForm
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import Textarea
from .models import *

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        labels = {'body':'Comment'}
        widgets = {
            'name': forms.TextInput(attrs={ 'class':"name-control", 'id':"name"}),
            'body': Textarea(attrs={ 'class':"body-control", 'id':"body"})
            }
