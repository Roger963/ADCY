	
from django.db import models

class Hospital(models.Model):
    sucursal = models.CharField(max_length=200, verbose_name="la sucursal")
    adress = models.CharField(max_length=200, verbose_name="la direccion")
    def __str__(self):
        return self.sucursal



class Especialidad(models.Model):
    hostpital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=30, verbose_name="La especialidad")
    estado = models.CharField(max_length=30, verbose_name="El estado")
    def __str__(self):
        return self.especialidad


class Medico(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    apellido = models.CharField(max_length=200, verbose_name="Apellido")
    telefone = models.IntegerField(verbose_name="Teléfono")
    estado = models.CharField(max_length=200, verbose_name="El estado")
    especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE, verbose_name="La especialidad")
    def __str__(self):
        return self.name

	
	