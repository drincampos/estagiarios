from django.shortcuts import render, get_object_or_404
from estagiarios.models import Estagiario, UnidadesCLDF

def index(request):
    return render(request, 'index.html')


