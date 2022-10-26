from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cartelera/', views.cartelera, name='cartelera'),
    path('detalle_pelicula/<str:pelicula>/', views.detalle_pelicula, name='detalle_pelicula'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
]