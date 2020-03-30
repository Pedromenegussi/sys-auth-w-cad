from django.shortcuts import render, redirect
from .models import dono_pet, pet
from django import forms
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
import requests
import agenda.templates


def index(request, template_name='registration/login.html'):
    print('/')
    return render(request, template_name)

@login_required
def painel_adm(request, template_name='painel_adm.html'):
    print('painel')
    return render(request, template_name)

