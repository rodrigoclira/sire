from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.generic import TemplateView
from .forms import RequerimentoForm
from .models import Despacho, Requerimento, Curso, TipoRequerimento

def index(request):    
    context = { }
    return render(request, 'requerimentos/index.html', context)

def resultado(request, new_context):
    return render(request, 'requerimentos/resultado.html', new_context)

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
            message = "Sucesso"            
        else:
            message = "error"

        context['message']: message
        
        response = resultado(request, context)
        return response

def buscar(request):    
    context = { }
    return render(request, 'requerimentos/pesquisar.html', context)    

def foo(request):
    context = {}
    print (request.POST)
    return render(request, 'requerimentos/index.html', context)

@login_required
def novos(request):
    requerimentos_novos = Requerimento.objects.exclude(pk__in = list(Despacho.objects.all().values_list('requerimento', flat=True)))
    
    #despachos = Despacho.objects.filter(proximo = request.user) #Errado    
    context = {
        'requerimentos': requerimentos_novos,
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