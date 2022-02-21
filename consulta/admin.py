from django.contrib import admin
from .models import Paciente, SintomasPaciente, Cita
class PacienteAdmin(admin.ModelAdmin):
    pass
class SintomasPacienteAdmin(admin.ModelAdmin):
    pass
class CitaAdmin(admin.ModelAdmin):
    pass
admin.site.register(Paciente)
admin.site.register(SintomasPaciente)
admin.site.register(Cita)