from django.contrib import admin
from .models import Paciente, SintomasPaciente, Cita
admin.site.register(Paciente)
admin.site.register(SintomasPaciente)
admin.site.register(Cita)