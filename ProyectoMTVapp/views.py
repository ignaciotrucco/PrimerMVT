from django.shortcuts import render
from .models import Familiares

# Create your views here.
def lista_familiares(request):
    lista_familiares = Familiares.objects.all()
    return render(request, 'ProyectoMTVapp/lista_familiares.html', context={"familiares": lista_familiares})