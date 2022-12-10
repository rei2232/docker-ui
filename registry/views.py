from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Registry
from .forms import RegistryForm
from django import forms
import docker_client
from django.contrib import messages
import logging
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)
@login_required
def index(request):
    models = Registry.objects.order_by('-pub_date')
    return render(request, 'registry/index.html', {'models': models})

@login_required
def detail(request, id):
    model = get_object_or_404(Registry, pk=id)
    return render(request, 'registry/detail.html', {'model': model})

@login_required
def create(request):
    if request.method == 'POST':
        form = RegistryForm(request.POST)
        if form.is_valid():
            try:
                if form.cleaned_data['authentication']:
                    res = docker_client.login(form.cleaned_data['instance_url'],
                                              form.cleaned_data['username'],
                                              form.cleaned_data['password'])
            except Exception as e:
                raise forms.ValidationError(e)
            model = form.save()
            return redirect('registry:detail', model.pk)
    else:
        form = RegistryForm()
    return render(request, 'registry/create.html', {'form': form})

@login_required
def update(request, id):
    model = get_object_or_404(Registry, pk=id)
    form = RegistryForm(request.POST or None, instance=model)
    if request.method == 'POST':
        if form.is_valid():
            try:
                res = docker_client.login(form.cleaned_data['instance_url'],
                                          form.cleaned_data['username'],
                                          form.cleaned_data['password'])
            except Exception as e:
                raise forms.ValidationError(e)

            model = form.save()
            return redirect('registry:detail', model.pk)
        else:
            form = RegistryForm(model)
    return render(request, 'registry/edit.html', {'form': form, 'model': model})

@login_required
def delete(request, id):
    model = get_object_or_404(Registry, pk=id)
    model.delete()
    return redirect('registry:index')
