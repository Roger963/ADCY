from ast import Delete
from django.db import models
from entidad.models import Medico

class Paciente(models.Model):
    name = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.IntegerField()
    cedula = models.IntegerField()
    address = models.CharField(max_length=200)

class SintomasPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    sintomas = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    discapacidad = models.BooleanField(default=False)
    tipoDescapacidad = models.CharField(max_length=200)
    grupSanguineo = models.CharField(max_length=200)
    

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=Delete)
    medico = models.OneToOneField(Medico, on_delete=models.CASCADE)
    turno = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=200)
	