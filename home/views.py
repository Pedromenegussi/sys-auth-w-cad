from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from home.models import *
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import  login, authenticate, logout
from django.contrib.auth.decorators import login_required

class PessoaForm(ModelForm):
    class Meta():
        model = Pessoa
        fields = ['nome', 'sobrenome', 'nascimento', 'email', 'usuario', 'senha']


@login_required
def pessoa_lista(request, template_name= 'pessoa_list.html'):
    pessoa = Pessoa.objects.all()
    data = {'lista': pessoa}
    return render(request, template_name, data)

def pessoa_create(request, template_name = 'form_pessoa.html'):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('login/')
    return render(request, template_name, {'form': form})

@login_required
def pessoa_edit(request, pk, template_name='pessoa_edit.html'):
    pessoa = get_object_or_404(Pessoa, pk=pk)
    if request.method == "POST":
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('pessoa_list')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, template_name, {'form': form})

@login_required
def pessoa_delete(request, pk):
    post = get_object_or_404(Pessoa, pk=pk)
    post.delete()
    return redirect('pessoa_list')


@csrf_protect
def pessoa_login(request, template_name="pessoa_login.html"):
    if request.method == 'POST':
        user = authenticate(usuario = request.POST['usuario'], senha = request.POST['senha'])
        if user is not None:
            login(request, user)
            return redirect('auth/')
    return render(request, template_name)

@login_required
def acesso(request, template_name="acess_user.html"):
    return render(request, template_name)


