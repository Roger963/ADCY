	
from django.db import models

class Hospital(models.Model):
    sucursal = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)

    def __str__(self):
        return self.sucursal

class Especialidad(models.Model):
    hostpital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)
    
    def __str__(self):
        return self.especialidad

class Medico(models.Model):
    name = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefone = models.IntegerField()
    estado = models.CharField(max_length=200)
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
	
	