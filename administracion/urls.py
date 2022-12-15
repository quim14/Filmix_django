from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('peliculas/', views.peliculas_index, name='peliculas'),
    path('peliculas/agregar', views.peliculas_agregar, name='peliculas_agregar'),
    path('peliculas/editar/<int:id_pelicula>', views.peliculas_editar, name='peliculas_editar'),
    path('peliculas/eliminar/<int:id_pelicula>', views.peliculas_eliminar, name='peliculas_eliminar'),


    path('funciones/', views.funciones, name='funciones'),
    path('funciones/agregar_funcion', views.funciones_agregar, name='funciones_agregar'),
    path('funciones/agregar_horario/<int:id_funcion>', views.horarios_agregar, name='horarios_agregar'),
    path('funciones/editar_horario/<int:id_funcion>/<int:id_horario>', views.horarios_editar, name='horarios_editar'),
    path('funciones/horarios/<int:id_funcion>', views.horarios, name='horarios'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)