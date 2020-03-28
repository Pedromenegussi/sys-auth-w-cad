"""agenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path
from home import views



urlpatterns = [
    url(r'^$',                      views.pessoa_create,                 name='pessoa_new'),
    url(r'^pessoa_list',            views.pessoa_lista,                  name='pessoa_list'),
    url(r'^editar/(?P<pk>[0-9]+)',  views.pessoa_edit,                   name='pessoa_edit'),
    url(r'^delete/(?P<pk>[0-9]+)',  views.pessoa_delete,                 name='pessoa_delete'),
    path('login/',                  views.pessoa_login,                  name='login'),
    path('auth/',                   views.acesso,                         name='acesso'),
]
