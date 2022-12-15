from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cartelera/', views.cartelera, name='cartelera'),
    path('detalle_pelicula/<int:id_pelicula>', views.detalle_pelicula, name='detalle_pelicula'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('logout/', auth_views.LogoutView.as_view(template_name='usuario/index.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)