from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from administracion.forms import PeliculaForm, PeliculaFormValidado, FuncionesForm, HorarioForm
from administracion.models import Pelicula
from administracion.models import Funcion, Horario


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
        # pelicula_form.save()
        return redirect('peliculas')
    
    else:
        pelicula_form = PeliculaForm()
    return render(request, "administracion/peliculas/agregar.html", {
        'pelicula_form':pelicula_form,
    })


@login_required(login_url=settings.LOGIN_URL)
def peliculas_editar(request, id_pelicula):
    if not request.user.groups.filter(name="administracion").exists():
        return render(request,'usuario/index.html')
    try:
        pelicula = Pelicula.objects.get(pk = id_pelicula)
    except Pelicula.DoesNotExist:
        return render(request, 'administracion/peliculas/peliculas.html')
    if (request.method == 'POST'):
        pelicula_form = PeliculaFormValidado(request.POST, instance=pelicula)
        # if pelicula_form.is_valid():
        # pelicula_form.save()
        nombre = request.POST['nombre']
        descripcion = request.POST['descripcion']
        trailer = request.POST['trailer']
        #poster = request.FILES['poster']
        pelicula.nombre = nombre
        pelicula.descripcion = descripcion
        pelicula.trailer = trailer
        pelicula.save()
        return redirect('peliculas')
    
    else:
        pelicula_form = PeliculaForm(instance=pelicula)
    return render(request, "administracion/peliculas/editar.html", {
        'pelicula_form':pelicula_form,
    })


#################################
# def funciones(request):
#     if not request.user.groups.filter(name="administracion").exists():
#         return render(request,'usuario/index.html')
#     # if (request.method == 'POST'):
#     #     funciones_form = FuncionesForm(request.POST)
#         return redirect('peliculas')
    
#     else:
#         pelicula_form = PeliculaForm(instance=pelicula)
#     return render(request, "administracion/peliculas/editar.html", {
#         'pelicula_form':pelicula_form,
#     })

@login_required(login_url=settings.LOGIN_URL)
def peliculas_eliminar(request, id_pelicula):
    if not request.user.groups.filter(name="administracion").exists():
        return render(request,'usuario/index.html')
    try:
        pelicula = Pelicula.objects.get(pk=id_pelicula)
    except Pelicula.DoesNotExist:
        return render(request, 'administracion/peliculas/peliculas.html')
    pelicula.soft_delete()
    return redirect('peliculas')


# class PeliculasListView(ListView)

#################################
@login_required(login_url=settings.LOGIN_URL)
def funciones(request):
    if not request.user.groups.filter(name="administracion").exists():
        return render(request,'usuario/index.html')
    funciones = Funcion.objects.all().order_by('-fecha')
    return render(request, "administracion/funciones/index.html", {'funciones': funciones,})

@login_required(login_url=settings.LOGIN_URL)
def funciones_agregar(request):
    if not request.user.groups.filter(name="administracion").exists():
        return render(request,'usuario/index.html')
    if (request.method == 'POST'):
        funcion_form = FuncionesForm(request.POST)
        # if funcion_form.is_valid():
        fecha = request.POST['fecha']
        pelicula = request.POST['pelicula']
        try:
            pelicula = Pelicula.objects.get(pk=pelicula)
        except Pelicula.DoesNotExist:
            return render(request, 'administracion/funciones/index.html')
        nueva_funcion = Funcion(fecha=fecha, pelicula=pelicula)
        nueva_funcion.save()
        return redirect('funciones')
    
    else:
        funcion_form = FuncionesForm()
    return render(request, "administracion/funciones/agregar_funcion.html", {
        'funcion_form':funcion_form,
    })

@login_required(login_url=settings.LOGIN_URL)
def horarios_agregar(request, id_funcion):
    if not request.user.groups.filter(name="administracion").exists():
        return render(request,'usuario/index.html')
    try:
        funcion = Funcion.objects.get(pk=id_funcion)
    except Funcion.DoesNotExist:
        return render(request, 'administracion/funciones/index.html')

    if (request.method == 'POST'):
        horario_form = HorarioForm(request.POST)
        # if horario_form.is_valid():
        hora = request.POST['hora']
        nuevo_horario = Horario(hora=hora, funcion=funcion)
        nuevo_horario.save()
        return redirect('funciones')
    
    else:
        horario_form = HorarioForm()
    return render(request, "administracion/funciones/agregar_horario.html", {
        'horario_form':horario_form, 'funcion':funcion,
    })


@login_required(login_url=settings.LOGIN_URL)
def horarios(request, id_funcion):
    if not request.user.groups.filter(name="administracion").exists():
        return render(request,'usuario/index.html')
    try:
        funcion = Funcion.objects.get(pk=id_funcion)
    except Funcion.DoesNotExist:
        return render(request, 'administracion/funciones/index.html')
    horas = Horario.objects.filter(funcion=funcion)
    return render(request, "administracion/funciones/horarios.html", {
        'funcion':funcion, 'horas':horas,
    })

@login_required(login_url=settings.LOGIN_URL)
def horarios_editar(request, id_funcion, id_horario):
    if not request.user.groups.filter(name="administracion").exists():
        return render(request,'usuario/index.html')
    try:
        hora = Horario.objects.get(pk = id_horario)
        funcion = Funcion.objects.get(pk=id_funcion)
    except Pelicula.DoesNotExist:
        return render(request, 'administracion/funciones/index')
    if (request.method == 'POST'):
    
        horario_form = HorarioForm(request.POST, instance=hora)
        # if pelicula_form.is_valid():
        # pelicula_form.save()
        hora = request.POST['hora']

        return redirect('funciones')
    
    else:
        horario_form = HorarioForm(instance=hora)
    return render(request, "administracion/funciones/editar_horario.html", {
        'horario_form':horario_form, 'funcion':funcion
    })
