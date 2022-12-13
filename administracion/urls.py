from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('peliculas/', views.peliculas_index, name='peliculas'),
    path('peliculas/agregar', views.peliculas_agregar, name='peliculas_agregar'),

    path('funciones/', views.funciones, name='funciones'),
    path('funciones/agregar_funcion', views.funciones_agregar, name='funciones_agregar')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)