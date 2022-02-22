from rest_framework import serializers
from .models import Examen

class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examen
        fields = ('descripcion', 'estado', 'costo', 'cita')