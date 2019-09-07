from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import RequerimentoForm
from .models import Despacho, Requerimento, Curso

def index(request):    
    context = { }
    return render(request, 'requerimentos/index.html', context)


class RequerimentoFormView(TemplateView):
    template_name = 'requerimentos/criar.html'

    def get(self, request):
        form = RequerimentoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = RequerimentoForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            print(nome)
            message = "Sucesso"

        context = {"forms": form, 'message': message }
        return render(request, self.template_name, context)

def buscar(request):    
    context = { }
    return render(request, 'requerimentos/pesquisar.html', context)    

def foo(request):
    context = {}
    print (request.POST)
    return render(request, 'requerimentos/index.html', context)

@login_required
def novos(request):
    despachos = Despacho.objects.filter(proximo = request.user) #Errado
    print (despachos)
    context = {
        'despachos': despachos,
        'novos': True,    
    }
    return render(request, 'requerimentos/listar.html', context)

@login_required
def responder(request, requerimento_id):
    requerimento = get_object_or_404(Requerimento, pk = requerimento_id) 
    despachos = Despacho.objects.filter(requerimento = requerimento)
    context = {
        'requerimento': requerimento,
        'despachos': despachos,        
    }
    print (despachos)
    return render(request, 'requerimentos/detalhar.html', context)

@login_required
def editar(request, requerimento_id):
    requerimento = get_object_or_404(Requerimento, pk = requerimento_id) 
    despachos = Despacho.objects.filter(requerimento = requerimento)
    context = {
        'requerimento': requerimento,
        'despachos': despachos,        
        'editar': True,
    }
    print (despachos)
    return render(request, 'requerimentos/detalhar.html', context)

@login_required
def historico(request):
    despachos = Despacho.objects.filter(despachante = request.user)
    print (despachos)
    context = {
        'despachos': despachos,
        'historico': True,
        }
    return render(request, 'requerimentos/listar.html', context)