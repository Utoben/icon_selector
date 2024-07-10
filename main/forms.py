from django import forms
from .models import *
from django.forms import ModelForm, TextInput, Textarea, ValidationError





class AddImageForm(forms.Form):
    image = forms.ImageField()