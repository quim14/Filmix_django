from django.shortcuts import redirect, render
from django.http import HttpResponse
from administracion.forms import *
from administracion.models import Pelicula


# Create your views here.


########### P E L I C U L A S ##############
def peliculas_index(request):
    peliculas = Pelicula.objects.filter(baja=False)
    return render(request, "administracion/peliculas/peliculas.html", {'peliculas':peliculas})

def peliculas_agregar(request):
    if (request.method == 'POST'):
        pelicula_form = PeliculaForm(request.POST)
        # if pelicula_form.is_valid():
        nombre = pelicula_form.cleaned_data['nombre']
        descripcion = pelicula_form.cleaned_data['descripcion']
        trailer = pelicula_form.cleaned_data['trailer']
        nueva_pelicula = Pelicula(nombre=nombre, descripcion=descripcion, trailer=trailer)
        nueva_pelicula.save()
        return redirect('peliculas')
    
    else:
        pelicula_form = PeliculaForm()
    return render(request, "administracion/peliculas/agregar.html", {
        'pelicula_form':pelicula_form,
    })




#################################
def funciones(request):
    if (request.method == 'POST'):
        funciones_form = FuncionesForm(request.POST)
    
    else:
        funciones_form = FuncionesForm()
    return render(request, "administracion/funciones.html", {
    'funciones_form': funciones_form,
    })
