from .models import *

from django import forms
from django.forms import ModelForm, TextInput, Textarea, ValidationError
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'user'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '******'}))

class AddImageForm(forms.Form):
    image = forms.ImageField()