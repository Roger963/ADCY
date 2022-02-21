from django.contrib import admin
from .models import Examen

class ExamenAdmin(admin.ModelAdmin):
    pass    
admin.site.register(Examen)