from rest_framework import serializers
from .models import Paciente, SintomasPaciente, Cita

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ('name', 'apellido', 'telefono', 'cedula', 'adress')


class SintomasPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SintomasPaciente
        fields = ('sintomas', 'descripcion', 'discapacidad', 'tipoDescapacidad', 'grupoSanguineo')

class CitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cita
        fields = ('paciente', 'medico', 'turno','fecha','estado')