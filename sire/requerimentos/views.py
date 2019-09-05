from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Despacho

def index(request):    
    context = { }
    return render(request, 'requerimentos/index.html', context)

def create(request):    
    context = { }
    return render(request, 'requerimentos/criar.html', context)

def search(request):    
    context = { }
    return render(request, 'requerimentos/pesquisar.html', context)    

@login_required
def list_req(request):
    despachos = Despacho.objects.filter(proximo = request.user)
    print (despachos)
    context = {'despachos': despachos}
    return render(request, 'requerimentos/listar.html', context)

@login_required
def edit_despacho(request):
    pass