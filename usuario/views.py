from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib import messages
from django.contrib.auth import authenticate, login

from usuario.formulario_registrarse import formulario_registro
from usuario.formulario_login import formulario_login

from administracion.models import Pelicula


def index(request):
    return render(request, "usuario/index.html")

def cartelera(request):
    peliculas = Pelicula.objects.filter(baja=False)
    return render(request, "usuario/cartelera.html", {'peliculas':peliculas})

def detalle_pelicula(request, id_pelicula):
    try:
        pelicula = Pelicula.objects.get(pk = id_pelicula)
    except Pelicula.DoesNotExist:
        return render(request, 'usuario/index.html')
    return render(request, "usuario/detalle_pelicula.html", {"pelicula":pelicula})


def registrarse(request):
    mensaje_exito = None
    mensaje_error = None
    if request.method == 'POST':
        formulario_1 = formulario_registro(request.POST)
        if formulario_1.is_valid():
            formulario_1.save()
            mensaje_exito = "Registro realizado con éxito"
        else:
            mensaje_error = "Error al completar el formulario"
    else:
        formulario_1 = formulario_registro()

    return render(request, "usuario/registrarse.html",
    {'formulario_1':formulario_1, 'mensaje_exito':mensaje_exito, 'mensaje_error':mensaje_error} )
    

def inicio_sesion(request):
    mensaje_login = None
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            nxt = request.GET.get('next', None)
            if nxt is None:
                return redirect('index')
            else:
                return redirect(nxt)
        else:
            mensaje_login = "Usuario o contraseña incorrecto"
            """ messages.error(request, f'Cuenta o contraseña incorrecto') """
    form = formulario_login()
    return render(request, "usuario/inicio_sesion.html", {'form':form, 'mensaje':mensaje_login})



# Create your views here.


# ------------SUPERADO------------

""" def registrarse(request):
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
    {'formulario_1':formulario_1, 'mensaje':mensaje} ) """