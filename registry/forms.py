from django import forms
from .models import Registry
from django.forms import CharField, CheckboxInput, PasswordInput, TextInput


class RegistryForm(forms.ModelForm):
    password = CharField(label='Password', widget=PasswordInput(attrs={'class': 'form-control'}), required=True, min_length=4, max_length=100)

    class Meta:
        model = Registry
        fields = ['name', 'instance_url', 'project_path', 'authentication', 'username']
        widgets = {
            'name': TextInput(attrs={
               'class': 'form-control'
            }),
            'instance_url': TextInput(attrs={
               'class': 'form-control' 
            }),
            'project_path': TextInput(attrs={
               'class': 'form-control'
            }),
            'authentication': CheckboxInput(attrs={
               'class': 'form-check-input' 
            }),
            'username': TextInput(attrs={
               'class': 'form-control' 
            }),
        }
