from django.shortcuts import render, redirect, get_object_or_404
from .models import Container
from .forms import ContainerForm
from registry.models import Registry
from django import forms
from django.contrib.auth.decorators import login_required
import docker_client
import logging
import json

logger = logging.getLogger(__name__)


@login_required
def index(request):
    models = docker_client.container_list()
    return render(request, 'containers/index.html', {'models': models})

@login_required
def detail(request, id):
    model = docker_client.container_get(id)
    json_attr = json.dumps(model.attrs)
    return render(request, 'containers/detail.html', {'model': model, 'inspect': model.attrs, 'json_attr': json_attr})

@login_required
def create(request):
    if request.method == 'POST':
        form = ContainerForm(request.POST)
        if form.is_valid():
            # envs = json.loads(form.cleaned_data['envs'])
            ports = json.loads(form.cleaned_data['ports'])

            docker_container = docker_client.container_create(form.cleaned_data['name'],
                                                              form.cleaned_data['image'].tags[2:-2],
                                                            #   envs,
                                                              ports)

            return redirect('containers:detail', docker_container.id)
    else:
        form = ContainerForm()
    return render(request, 'containers/create.html', {'form': form})

@login_required
def delete(request, id):
    docker_client.container_remove(id)
    return redirect('containers:index')

@login_required
def start(request, id):
    docker_client.container_start(id)
    return redirect('containers:detail', id)

@login_required
def stop(request, id):
    docker_client.container_stop(id)
    return redirect('containers:detail', id)

@login_required
def kill(request, id):
    docker_client.container_kill(id)
    return redirect('containers:detail', id)

@login_required
def restart(request, id):
    docker_client.container_restart(id)
    return redirect('containers:detail', id)

@login_required
def pause(request, id):
    docker_client.container_pause(id)
    return redirect('containers:detail', id)

@login_required
def resume(request, id):
    docker_client.container_resume(id)
    return redirect('containers:detail', id)

@login_required
def logfollow(request, id):
    lines = request.GET.get("lines", "100")

    try:
        lines = int(lines)
    except Exception as e:
        lines = "all"
    log = docker_client.container_logs(id, lines)
    return render(request, 'containers/logs.html', {'id': id, 'log': log.decode("utf-8"), 'lines': lines})
