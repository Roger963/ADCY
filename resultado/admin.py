from django.contrib import admin
from .models import Examen

class ExamenAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'estado', 'cita', 'costo')
    search_fields = ('descripcion', 'cita')   
admin.site.register(Examen, ExamenAdmin)