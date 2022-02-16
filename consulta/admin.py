from django.contrib import admin
from .models import Paciente, Cita


admin.site.register(Cita)
admin.site.register(Paciente)
