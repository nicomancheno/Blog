from django.forms import ModelForm
from django import forms
from .models import *

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
            'name': forms.TextInput(attrs={ 'class':"form-control", 'id':"lastName"}),
            'body': forms.TextInput(attrs={ 'class':"form-control", 'id':"address"})
            }
