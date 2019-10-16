from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import RequerimentoForm
from .models import Despacho, Requerimento, Curso, TipoRequerimento, UsuarioFuncao
from django.conf import settings
from django.contrib.auth.models import User



class RequerimentoFormView(TemplateView):
    template_name = 'requerimentos/criar.html'

    def get(self, request):
        form = RequerimentoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RequerimentoForm(request.POST)
        context = {}
        
        if form.is_valid():
            requerimento = form.save(commit = False)

            curso_value = form.cleaned_data['curso']
            curso_object = Curso.objects.get(sigla = curso_value)
            requerimento.curso = curso_object
            
            tipo_value = form.cleaned_data['tipo']
            print(tipo_value)
            tipo_object = TipoRequerimento.objects.get(pk = int(tipo_value))
            requerimento.tipo = tipo_object

            requerimento.save()

        return redirect('resultado')


def index(request):    
    context = { }
    return render(request, 'requerimentos/index.html', context)

def resultado(request):
    return render(request, 'requerimentos/resultado.html')


def buscar(request):    
    context = { }
    return render(request, 'requerimentos/pesquisar.html', context)    

def foo(request):
    context = {}
    print (request.POST)
    return render(request, 'requerimentos/index.html', context)


## Required Views
@login_required
def novos(request):
    usuarioPrioridades = list(UsuarioFuncao.objects.filter(usuario = request.user).values_list("funcao__prioridade"))    
    usuarioPrioridades = [prioridade[0] for prioridade in usuarioPrioridades if prioridade]    
    requerimentos = []

    if (settings.PRIORIDADE_PRIMEIRO_DESPACHO in usuarioPrioridades):
        requerimentos = Requerimento.objects.exclude(pk__in = list(Despacho.objects.all().values_list('requerimento', flat=True)))
        print (requerimentos)
    
    
    #despachos = Despacho.objects.filter(proximo = request.user) #Errado    
    context = {
        'requerimentos': requerimentos,
        'novos': True,    
    }
    return render(request, 'requerimentos/listar.html', context)

@login_required
def responder(request, requerimento_id):

    requerimento = get_object_or_404(Requerimento, pk = requerimento_id) 
    despachos = Despacho.objects.filter(requerimento = requerimento)
    usuarios = User.objects.all()

    context = {
        'requerimento': requerimento,
        'despachos': despachos,
        'usuarios': usuarios,        
    }
    print (despachos)

    if request.POST:
        data = request.POST.dict()
        despacho = Despacho()
        despacho.requerimento = requerimento
        despacho.conteudo = data.get('despacho')
        print(data.get('proximo'))
        despacho.proximo = get_object_or_404(User, pk = data.get('proximo'))
        despacho.despachante = request.user
        despacho.save()

        print (despacho) 

    return render(request, 'requerimentos/detalhar.html', context)

@login_required
def editar(request, requerimento_id):
    requerimento = get_object_or_404(Requerimento, pk = requerimento_id) 
    despachos = Despacho.objects.filter(requerimento = requerimento)
    usuarios = User.objects.all()

    context = {
        'requerimento': requerimento,
        'despachos': despachos,        
        'editar': True,
        'usuarios': usuarios,
    }

    print (despachos)
    print (context)
    return render(request, 'requerimentos/detalhar.html', context)

@login_required
def historico(request):
    despachos = Despacho.objects.filter(despachante = request.user)
    context = {
        'despachos': despachos,
        'historico': True,
        }
    return render(request, 'requerimentos/listar.html', context)