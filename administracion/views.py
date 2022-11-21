from django.shortcuts import render
from django.http import HttpResponse
from administracion.forms import PeliculaForm

# Create your views here.

def peliculas(request):
    if (request.method == 'POST'):
        pelicula_form = PeliculaForm(request.POST)
    
    else:
        pelicula_form = PeliculaForm()
    return render(request, "administracion/peliculas.html", {
        'pelicula_form':pelicula_form,
    })
