from rest_framework import serializers
from .models import Hospital, Especialidad, Medico

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = ('sucursal','adress')


class EspecialidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidad
        fields = ('especialidad','estado')


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ('name','apellido','telefone','estado')
