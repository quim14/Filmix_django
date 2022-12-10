from django.db import models

# Create your models here.

""" class usuario(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    mail = models.EmailField(verbose_name='Email')
    contraseña = models.CharField(max_length=100, verbose_name='Contraseña')
    baja = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.apellido}, {self.nombre} '

    def soft_delete(self):
        self.baja = True
        super().save()

    def restore(self):
        self.baja = False
        super().save()

 """
 
""" class pelicula(models.Model):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    # imagen = models.ImageField(verbose_name='Imagen')
    fecha_ini = models.DateField(verbose_name='Fecha de Inicio')
    fecha_fin = models.DateField(verbose_name='Fecha de Fin')
    horarios = 
    duracion = models.DurationField(verbose_name='Duracion')
    descripcion = models.TextField(verbose_name='Descripcion')
    trailer = models.SlugField(verbose_name='Trailer')
    
 """

""" var pelicula_0 = {
    id: 1,
    nombre: "Granizo",
    imagen: "./img/Peliculas/Granizo.jpg",
    fecha_ini: "01/03/2022",
    fecha_fin: "31/12/2022",
    horarios: ["20:00","22:00"],
    descripcion: "Un famoso meteorólogo de la televisión se convierte en el enemigo público número uno cuando no logra evitar una terrible tormenta de granizo.",
    trailer: "https://www.youtube.com/embed/-F2watcvQQs",
} """