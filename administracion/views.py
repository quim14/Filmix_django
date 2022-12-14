from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from administracion.forms import PeliculaForm
from administracion.models import Pelicula
from administracion.models import Funcion


# Create your views here.


########### P E L I C U L A S ##############
@login_required(login_url=settings.LOGIN_URL)
def peliculas_index(request):
    if not request.user.groups.filter(name="administracion").exists():
        return render(request,'usuario/index.html')
    peliculas = Pelicula.objects.filter(baja=False)
    return render(request, "administracion/peliculas/peliculas.html", {'peliculas':peliculas})

@login_required(login_url=settings.LOGIN_URL)
def peliculas_agregar(request):
    if not request.user.groups.filter(name="administracion").exists():
        return render(request,'usuario/index.html')
    if (request.method == 'POST'):
        pelicula_form = PeliculaForm(request.POST)
        # if pelicula_form.is_valid():
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        trailer = request.POST['trailer']
        poster = request.FILES['poster']
        nueva_pelicula = Pelicula(nombre=nombre, descripcion=descripcion, trailer=trailer, poster=poster)
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
    if not request.user.groups.filter(name="administracion").exists():
        return render(request,'usuario/index.html')
    # if (request.method == 'POST'):
    #     funciones_form = FuncionesForm(request.POST)
    
    # else:
    #     funciones_form = FuncionesForm()
    funciones = Funcion.objects.all().order_by('-fecha')
    return render(request, "administracion/funciones/index.html", {'funciones': funciones,})


def funciones_agregar(request):
    if not request.user.groups.filter(name="administracion").exists():
        return render(request,'usuario/index.html')
    return render(request, "administracion/funciones/agregar_funcion.html", {
        'pelicula_form':'pelicula_form',
    })
