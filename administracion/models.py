from django.db import models
from datetime import date

# Create your models here.

class Pelicula(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    trailer = models.CharField(max_length=150, verbose_name='Trailer')
    descripcion = models.TextField(verbose_name='Descripcion')
    baja = models.BooleanField(default=0)
    poster = models.ImageField(upload_to="posters", null=True)

    def __str__(self):
        return self.nombre
    
    # DAR BAJA LOGICA
    def soft_delete(self):
        self.baja=True
        super().save()
    
    def restore(self):
        self.baja=False
        super().save()
    
class Funcion(models.Model):
    fecha = models.DateField(verbose_name='Fecha', default=date.today())
    pelicula = models.ForeignKey(Pelicula, on_delete=models.RESTRICT, related_name='peliculas')
    # baja = models.BooleanField(default=0)

    # def soft_delete(self):
    #     self.baja=True
    #     super().save()
    
    # def restore(self):
    #     self.baja=False
    #     super().save()


class Horario(models.Model):
    hora = models.TimeField(auto_now=False, auto_now_add=False ,verbose_name='Hora')
    funcion = models.ForeignKey(Funcion, on_delete=models.CASCADE, related_name='horarios')
    # baja = models.BooleanField(default=0)

    # def soft_delete(self):
    #     self.baja=True
    #     super().save()
    
    # def restore(self):
    #     self.baja=False
    #     super().save()
