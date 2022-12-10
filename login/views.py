from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
import logging

logger = logging.getLogger(__name__)


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        logger.info(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'Successfully logged in.')
            return redirect('images:index')
        else:
            messages.error(request, 'Try again.')
            return redirect('login:index')
    else: 
        return render(request, 'login/index.html', {})
def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out.')
    return redirect('login:index')