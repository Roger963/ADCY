from django.db import models

class Hospital(models.Model):
    sucursal = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)

class Especialidad(models.Model):
    especialidad = models.CharField(max_length=30)
    estado = models.CharField(max_length=30)

class Medico(models.Model):
    name = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    telefone = models.IntegerField()
    estado = models.CharField(max_length=200)
    id_hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)