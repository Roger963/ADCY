from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PacienteSerializer, SintomasPacienteSerializer, Cita
from .models import Paciente, SintomasPaciente, Cita
# Create your views here.
class PacienteView(viewsets.ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Paciente.objects.all()

class SintomasPacienteView(viewsets.ModelViewSet):
    serializer_class = SintomasPacienteSerializer
    queryset = SintomasPaciente.objects.all()

class CitaView(viewsets.ModelViewSet):
    serializer_class = CitaSerializer
    queryset = Cita.objects.all()