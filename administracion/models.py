from django.db import models

# Create your models here.

class Pelicula(models.Model):
    ESTADOS_PELICULA = (
        ('D', 'Disponible'),
        ('N', 'No disponible'),
    )
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    trailer = models.CharField(max_length=150, verbose_name='Trailer')
    descripcion = models.TextField(null=True, verbose_name='Descripcion')
    poster = models.CharField(max_length=100, verbose_name='Poster')
    estado = models.CharField(max_length=1, verbose_name='Estado', choices=ESTADOS_PELICULA)
    baja = models.BooleanField(default=0)

    def __str__(self):
        return self.nombre
    
    # DAR BAJA LOGICA
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
    
