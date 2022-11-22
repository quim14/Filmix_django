from django.shortcuts import render
from django.http import HttpResponse
from administracion.forms import *

# Create your views here.

def peliculas(request):
    if (request.method == 'POST'):
        pelicula_form = PeliculaForm(request.POST)
    
    else:
        pelicula_form = PeliculaForm()
    return render(request, "administracion/peliculas.html", {
        'pelicula_form':pelicula_form,
    })

def funciones(request):
    if (request.method == 'POST'):
        funciones_form = FuncionesForm(request.POST)
    
    else:
        funciones_form = FuncionesForm()
    return render(request, "administracion/funciones.html", {
    'funciones_form': funciones_form,
    })
