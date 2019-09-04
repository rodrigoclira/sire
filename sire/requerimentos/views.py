from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def index(request):    
    context = { }
    return render(request, 'requerimentos/index.html', context)


@login_required
def listar(request):
    return HttpResponse("Você estará vendo a lista de requerimentos")
