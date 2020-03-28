from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.contrib import messages
from django.forms import ModelForm
from home.models import *
from django.views.decorators.csrf import csrf_protect
from agenda.settings import  LOGOUT_REDIRECT_URL


class PessoaForm(ModelForm):
    class Meta():
        model = Pessoa
        fields = ['nome', 'sobrenome', 'nascimento', 'email', 'usuario', 'senha']


def pessoa_lista(request, template_name= 'pessoa_list.html'):
    pessoa = Pessoa.objects.all()
    data = {'lista': pessoa}
    return render(request, template_name, data)


def pessoa_create(request, template_name = 'form_pessoa.html'):
    form = PessoaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('pessoa_list')
    return render(request, template_name, {'form': form})


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


def pessoa_delete(request, pk):
    post = get_object_or_404(Pessoa, pk=pk)
    post.delete()
    return redirect('pessoa_list')


def login_user(request, template_name='pessoa_login.html'):
    return render(request, template_name)

@csrf_protect
def pessoa_login(request, template_name = 'pessoa_login.html'):
    if request.POST:
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        pessoa = get_object_or_404(Pessoa, usuario=usuario, senha=senha)
        if pessoa is not None:
            print('Acesso!')
            return redirect('acesso')
        else:
            messages.error(request, 'Usuário/Senha inválidos. Favor tentar novamente.')
            return redirect('/')
    else:
        return redirect(request, template_name)

def acesso(request, template_name="acess_user.html"):
    return render(request, template_name)


def desconecta(request, template_name="pessoa_login.html"):
    return render(request, template_name)