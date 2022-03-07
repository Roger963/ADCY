
from django.db import models

from consulta.models import Cita

class Examen(models.Model):
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion")
    estado = models.CharField(max_length=200, verbose_name="Estado")
    costo = models.IntegerField(verbose_name="Costo")
    cita = models.OneToOneField(Cita, on_delete=models.CASCADE, verbose_name="Cita")

    def __str__(self):
       return str(self.descripcion)
	
	
	
	
# Create your models 