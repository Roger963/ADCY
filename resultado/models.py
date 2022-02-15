from django.db import models

from consulta.models import Paciente

class Examen(models.Model):
    descripcion = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    costo = models.IntegerField()

class ExamenPaciente(models.Model):
    hora = models.DateField(blank=False, null=True)
    fecha = models.DateTimeField(auto_now=True)
    resultado = models.CharField(max_length=200)
    id_examen = models.ForeignKey(Examen,on_delete=models.CASCADE)
    id_paciente = models.ManyToManyField(Paciente)