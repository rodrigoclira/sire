from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Despacho, Requerimento, Curso

def index(request):    
    context = { }
    return render(request, 'requerimentos/index.html', context)

def criar(request):
    cursos = Curso.objects.all()     
    context = {'cursos': cursos}
    return render(request, 'requerimentos/criar.html', context)

def buscar(request):    
    context = { }
    return render(request, 'requerimentos/pesquisar.html', context)    

@login_required
def novos(request):
    despachos = Despacho.objects.filter(proximo = request.user) #Errado
    print (despachos)
    context = {'despachos': despachos}
    return render(request, 'requerimentos/listar.html', context)

@login_required
def resposta(request, requerimento_id):
    requerimento = get_object_or_404(Requerimento, pk = requerimento_id) #Errado
    
    context = {
        'requerimento': requerimento,
    }

    return render(request, 'requerimentos/detalhar.html', context)

@login_required
def historico(request):
    despachos = Despacho.objects.filter(proximo = request.user)
    print (despachos)
    context = {'despachos': despachos}
    return render(request, 'requerimentos/listar.html', context)