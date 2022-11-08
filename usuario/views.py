from django.shortcuts import render
from django.http import HttpResponse

from usuario.formulario_registrarse import formulario_registro

def index(request):
    return render(request, "usuario/index.html")

def cartelera(request):
    '''La variable peliculas_cartelera podria ser una lista que traiga diccionarios en donde se indique la información de las 
    películas que están en cartelera'''
    peliculas_cartelera = []
    return render(request, "usuario/cartelera.html", {"peliculas_cartelera": peliculas_cartelera})

def detalle_pelicula(request, pelicula):
    return render(request, "usuario/detalle_pelicula.html")


def registrarse(request):
    mensaje = None
    if(request.method == 'POST'):
        formulario_1 = formulario_registro(request.POST)
        if(formulario_1.is_valid()):

            # Aca agregar las acciones que deben hacerse al cargar el formulario
            mensaje = "Registro realizado con éxito"
        else:
            mensaje = "Error al completar el formulario"
    else:
        formulario_1 = formulario_registro()

    return render(request, "usuario/registrarse.html",
    {'formulario_1':formulario_1, 'mensaje':mensaje} )
    

def inicio_sesion(request):
    return render(request, "usuario/inicio_sesion.html")


# Create your views here.
