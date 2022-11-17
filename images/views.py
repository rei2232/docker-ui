from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Image
from .forms import ImageForm
from registry.models import Registry
from django import forms
import docker_client
import logging

logger = logging.getLogger(__name__)


def index(request):
    models = Image.objects.order_by('-pub_date')
    # docker_images = docker_client.image_list()
    return render(request, 'images/index.html', {'models': models})


def detail(request, id):
    model = get_object_or_404(Image, pk=id)
    inspect = docker_client.image_inspect(model.tags[2:-2])
    return render(request, 'images/detail.html', {'model': model, 'inspect': inspect})


def create(request):
    if request.method == 'POST':
        form = ImageForm(request.POST)
        if form.is_valid():
            logger.info(form.cleaned_data['repository'] + str(form.cleaned_data['tag']))
            docker_image = docker_client.image_pull(form.cleaned_data['repository'], str(form.cleaned_data['tag']))
            model = Image()
            model.repository = form.cleaned_data['repository']
            model.image_id = docker_image.id
            model.image_short_id = docker_image.id
            model.tags = docker_image.tags
            model.save()
            return redirect('images:detail', model.pk)
    else:
        form = ImageForm()
    return render(request, 'images/create.html', {'form': form})


def update(request, id):
    model = get_object_or_404(Image, pk=id)
    form = ImageForm(request.POST or None, instance=model)
    if request.method == 'POST':
        if form.is_valid():
            model = form.save()
            return redirect('images:detail', model.pk)
        else:
            form = ImageForm(model)
    return render(request, 'images/edit.html', {'form': form, 'model': model})


def delete(request, id):
    model = get_object_or_404(Image, pk=id)
    docker_client.image_remove(model.repository)
    model.delete()
    return redirect('images:index')
