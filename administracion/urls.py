from django.urls import path

from . import views

urlpatterns = [
    path('peliculas', views.peliculas),
]