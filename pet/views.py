from django.shortcuts import render, redirect
from .models import *
from django import forms
from django.contrib.auth import login, logout 
from django.contrib.auth.decorators import login_required
from . import models
import requests
import website

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Dono_pet
        fields = '__all__'


def login(request, template_name='registration/login.html'):
    print('/')
    return render(request, template_name)


@login_required
def index(request, template_name='index.html'):
    form = ClienteForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, template_name, context)

