from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from administracion.forms import PeliculaForm
from administracion.models import Pelicula


# Create your views here.


########### P E L I C U L A S ##############
@login_required(login_url=settings.LOGIN_URL)
def peliculas_index(request):
    peliculas = Pelicula.objects.filter(baja=False)
    return render(request, "administracion/peliculas/peliculas.html", {'peliculas':peliculas})

@login_required(login_url=settings.LOGIN_URL)
def peliculas_agregar(request):
    if (request.method == 'POST'):
        pelicula_form = PeliculaForm(request.POST)
        if pelicula_form.is_valid():
            nueva_pelicula = Pelicula()
            nueva_pelicula.nombre = pelicula_form.cleaned_data['nombre']
            nueva_pelicula.descripcion = pelicula_form.cleaned_data['descripcion']
            nueva_pelicula.trailer = pelicula_form.cleaned_data['trailer']
            nueva_pelicula.estado = 'D'
            nueva_pelicula.poster = 'C:'
            nueva_pelicula.save()
        return redirect('peliculas')
    
    else:
        pelicula_form = PeliculaForm()
    return render(request, "administracion/peliculas/agregar.html", {
        'pelicula_form':pelicula_form,
    })




#################################
@login_required(login_url=settings.LOGIN_URL)
def funciones(request):
    if (request.method == 'POST'):
        funciones_form = FuncionesForm(request.POST)
    
    else:
        funciones_form = FuncionesForm()
    return render(request, "administracion/funciones.html", {
    'funciones_form': funciones_form,
    })
