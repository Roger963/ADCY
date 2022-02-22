from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import HospitalSerializer, EspecialidadSerializer, MedicoSerializer
from .models import Hospital, Especialidad, Medico

# Create your views here.

class HospitalView(ModelViewSet):
    def get_queryset(self):
        queryset = Hospital.objects.all()
        serializers_class =HospitalSerializer
        return queryset.filter(owner=self.request.Hospital.owner)
    

class EspecialidadView(ModelViewSet):
    serializers_class = EspecialidadSerializer
    queryset = Especialidad.objects.all()

class MedicoView(ModelViewSet):
    serializers_class = MedicoSerializer
    queryset = Medico.objects.all()
