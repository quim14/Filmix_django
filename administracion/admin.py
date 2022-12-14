from django.contrib import admin

from administracion.models import Pelicula, Funcion, Horario

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'baja')
    search_fields = ['nombre']
    list_filter = ('baja',)

class FuncionAdmin(admin.ModelAdmin):
    pass

class HorarioAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Funcion, FuncionAdmin)
admin.site.register(Horario, HorarioAdmin)
