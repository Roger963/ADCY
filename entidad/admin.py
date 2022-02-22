from django.contrib import admin
from entidad.models import Hospital, Medico, Especialidad
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('name', 'apellido')
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('sucursal','adress')
class EspecialidadAdmin(admin.ModelAdmin):
    pass

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Hospital, HospitalAdmin)





