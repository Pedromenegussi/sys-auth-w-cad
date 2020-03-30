from django.shortcuts import render, redirect
from .models import Dono_bicho
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import login, logout
import requests
import agenda.templates

class PessoaForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


def index(request, template_name='registration/login.html'):
    print('passei')
    return render(request, template_name)


def logout(request, template_name='registration/logged_out.html'):
    print('desloguei')
    return render(requst, template_name)