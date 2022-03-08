from django.contrib import admin
from entidad.models import Hospital, Medico, Especialidad
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('name', 'apellido')
    search_fields = ('name', 'apellido')
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('sucursal','adress')
    search_fields = ('sucursal', 'adress')
class EspecialidadAdmin(admin.ModelAdmin):
    list_display = ('especialidad','estado')
    search_fields = ('especialidad', 'estado')

admin.site.register(Medico, MedicoAdmin)
admin.site.register(Especialidad, EspecialidadAdmin)
admin.site.register(Hospital, HospitalAdmin)





