from django import forms
from images.models import Image
from .models import Container
from django.forms import TextInput, ModelChoiceField, Select, CharField 

class ContainerForm(forms.Form):
    name = CharField(max_length=100, strip=True, required=True, widget=TextInput(attrs={'class': 'form-control'}))
    image = ModelChoiceField(queryset=Image.objects.all(), required=True,widget=Select(attrs={'class': 'form-control'}))
    ports = CharField(max_length=3000, required=False, strip=True,widget=TextInput(attrs={'class': 'form-control'}))
    envs = CharField(required=False, strip=True,widget=TextInput(attrs={'class': 'form-control'}))
