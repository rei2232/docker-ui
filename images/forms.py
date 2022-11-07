from django import forms
from .models import Image
from registry.models import Registry


class ImageForm(forms.ModelForm):
    registry = forms.ModelChoiceField(queryset=Registry.objects.all())

    class Meta:
        model = Image
        fields = ['repository']

    def clean_repository(self):
        data = str(Registry.objects.get(pk=self.data['registry'])) + self.data['repository']
        return data.lower()
