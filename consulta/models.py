from ast import Delete
from django.db import models
from entidad.models import Medico

class Paciente(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre")
    apellido = models.CharField(max_length=200, verbose_name="Apellido")
    telefono = models.IntegerField(verbose_name="Teléfono")
    cedula = models.IntegerField(verbose_name="Cedula")
    address = models.CharField(max_length=200, verbose_name="Direccion")
    def __str__(self):
        return self.name

class SintomasPaciente(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, verbose_name="Paciente")
    sintomas = models.CharField(max_length=200, verbose_name="Sintomas")
    descripcion = models.CharField(max_length=200, verbose_name="Descripcion")
    discapacidad = models.BooleanField(default=False, verbose_name="Discapcidad")
    tipoDescapacidad = models.CharField(max_length=200, verbose_name="tipo de discapacidad")
    grupSanguineo = models.CharField(max_length=200, verbose_name="Tipo de sangre")
    def __str__(self):
        return self.sintomas
    

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=Delete,verbose_name="Paciente")
    medico = models.OneToOneField(Medico, on_delete=models.CASCADE, verbose_name="Medico")
    turno = models.IntegerField(verbose_name="Turno")
    fecha = models.DateTimeField(auto_now_add=True, verbose_name="Fecha")
    estado = models.CharField(max_length=200, verbose_name="Estado")
   
	