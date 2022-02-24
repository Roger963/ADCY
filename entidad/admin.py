from django.contrib import admin
from entidad.models import Hospital, Medico, Especialidad
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('name', 'apellido')
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('sucursal','adress')
    search_fiels=('sucursal')
class EspecialidadAdmin(admin.ModelAdmin):
    pass

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Especialidad)
admin.site.register(Hospital, HospitalAdmin)





