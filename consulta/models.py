from django.db import models

from entidad.models import Medico
# Create your models here.
class Paciente(models.Model):
    name = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefono = models.IntegerField()
    cedula = models.IntegerField()
    address = models.CharField(max_length=200)
    

class Cita(models.Model):
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_medico = models.OneToOneField(Medico, on_delete=models.CASCADE)
    turno = models.IntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=200)