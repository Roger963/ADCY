from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ExamenSerializer
from .models import Examen
# Create your views here.
class ExamenView(viewsets.ModelViewSet):
    serializer_class = ExamenSerializer
    queryset = Examen.objects.all()