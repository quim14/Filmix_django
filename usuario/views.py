from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "usuario/index.html")

def cartelera(request):
    '''La variable peliculas_cartelera podria ser una lista que traiga diccionarios en donde se indique la información de las 
    películas que están en cartelera'''
    peliculas_cartelera = []
    return render(request, "usuario/cartelera.html", {"peliculas_cartelera": peliculas_cartelera})

def detalle_pelicula(request, pelicula):
    return HttpResponse(f'''Pagina de la película {pelicula}''')

def registrarse(request):
    return HttpResponse("Pagina de registro")

def inicio_sesion(request):
    return HttpResponse("Pagina de inicio de sesión")


# Create your views here.
