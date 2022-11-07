from django import forms
from .models import Registry


class RegistryForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput, min_length=4, max_length=100)

    class Meta:
        model = Registry
        fields = ['name', 'instance_url', 'project_path', 'authentication', 'username']
