from re import M
from django.contrib import admin
from .models import Hospital, Especialidad, Medico

admin.site.register(Hospital)
admin.site.register(Especialidad)
admin.site.register(Medico)