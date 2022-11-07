from django import forms
from images.models import Image


class ContainerForm(forms.Form):
    name = forms.CharField(max_length=100, strip=True, required=True)
    image = forms.ModelChoiceField(queryset=Image.objects.all(), required=True)
    ports = forms.CharField(max_length=3000, required=False, strip=True)
    envs = forms.CharField(required=False, strip=True)
