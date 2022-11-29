from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from usuario.formulario_registrarse import formulario_registro
from usuario.models import usuario

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
            nombre = formulario_1.cleaned_data['nombre']
            apellido = formulario_1.cleaned_data['apellido']
            mail = formulario_1.cleaned_data['mail']
            contraseña = formulario_1.cleaned_data['contraseña_1']
            nuevo_usuario = usuario(nombre=nombre, apellido=apellido, mail=mail, contraseña=contraseña)
            nuevo_usuario.save()
            

            # Aca agregar las acciones que deben hacerse al cargar el formulario
            mensaje = "Registro realizado con éxito"
        else:
            mensaje = "Error al completar el formulario"
    else:
        formulario_1 = formulario_registro()

    return render(request, "usuario/registrarse.html",
    {'formulario_1':formulario_1, 'mensaje':mensaje} )
    

def inicio_sesion(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not NONE:
            login(request, user)
            return redirect('index')
        else:
            message.error(request, f'Cuenta o contraseña incorrecto')
    form = AuthenticationForm()
    return render(request, "usuario/inicio_sesion.html", {'form':form})


# Create your views here.
