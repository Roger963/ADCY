
from django.db import models

from consulta.models import Cita

class Examen(models.Model):
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    costo = models.IntegerField()
    cita = models.OneToOneField(Cita, on_delete=models.CASCADE)

    def __str__(self):
        return self.descripcion 
	
	
	
	
# Create your models 