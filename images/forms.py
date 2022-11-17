from django import forms
from .models import Image
from registry.models import Registry
from django.forms import TextInput, ModelChoiceField, Select, IntegerField, NumberInput

class ImageForm(forms.ModelForm):
    registry = ModelChoiceField(queryset=Registry.objects.all(), widget=Select(attrs={'class': 'form-control'}))
    tag = IntegerField(label='Tag', required=True, widget=NumberInput(attrs={'class': 'form-control'})) 

    class Meta:
        model = Image
        fields = ['repository']
        widgets = {
            'repository': TextInput(attrs={
               'class': 'form-control'
            })
        }
