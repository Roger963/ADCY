from django.shortcuts import render
from .models import Medico, Paciente
# Create your views here.
def medicina(request):
    medicos_list = Medico.objects.all()
    return render(request, 'index.html', {
        'medicos_list': medicos_list,
    })

def paciente(request):
    paciente_list = Paciente.objects.all()
    return render(request, 'index.html', {
        'paciente_list': paciente_list,
    })