from django.contrib import admin

from .models import Examen, ExamenPaciente

admin.site.register(Examen)
admin.site.register(ExamenPaciente)