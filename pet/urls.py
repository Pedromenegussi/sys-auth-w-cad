"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.pet, name='pet')
Class-based views
    1. Add an import:  from other_app.views import Pet
    2. Add a URL to urlpatterns:  path('', Pet.as_view(), name='pet')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from pet import views
from django.contrib import admin


urlpatterns = [
    path('',    views.index, name='index'),
    path('painel_adm', views.painel_adm, name='painel.html'),

]

