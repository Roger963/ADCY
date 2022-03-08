from django.urls import path
from . import views

urlpatterns = [
    path("medicos/",views.medicina, name="index"),
#    path("turnos/",views.index, name="index"),

]
