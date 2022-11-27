from django.urls import path

from . import views

urlpatterns = [
    path('peliculas/', views.peliculas_index, name='peliculas'),
    path('peliculas/agregar', views.peliculas_agregar, name='peliculas_agregar'),


    path('funciones/', views.funciones, name='funciones')
]