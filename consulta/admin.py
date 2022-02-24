from django.contrib import admin
from .models import Paciente, SintomasPaciente, Cita
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'apellido', 'telefono', 'address')
class SintomasPacienteAdmin(admin.ModelAdmin):
    list_display = ('sintomas', 'descripcion','discapacidad','tipoDescapacidad')
class CitaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'medico','turno','turno','fecha','estado')
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(SintomasPaciente)
admin.site.register(Cita)