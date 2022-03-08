from django.contrib import admin
from .models import Paciente, SintomasPaciente, Cita
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'apellido', 'telefono', 'address')
    search_fields = ('name', 'apellido')  
class SintomasPacienteAdmin(admin.ModelAdmin):
    list_display = ('sintomas', 'descripcion','discapacidad','tipoDescapacidad')
    search_fields = ('sintomas', 'descripcion')
class CitaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico','turno','turno','fecha','estado')
    search_fields = ('paciente', 'turno')
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(SintomasPaciente, SintomasPacienteAdmin)
admin.site.register(Cita, CitaAdmin)