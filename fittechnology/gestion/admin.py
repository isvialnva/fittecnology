from django.contrib import admin
from .models import Clasificacion, DatosPersona


class ClasificacionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion')
    search_fields = ['codigo', 'descripcion']
    ordering = ['codigo']
    list_per_page = 50


class DatosPersonaAdmin(admin.ModelAdmin):
    list_display = ('tipo_identificacion', 'identificacion', 'primer_nombre', 'segundo_nombre', 'primer_apellido',
                    'segundo_apellido')
    search_fields = ['identificacion', 'primer_nombre', 'primer_apellido']
    ordering = ['identificacion']
    list_per_page = 50


admin.site.register(Clasificacion, ClasificacionAdmin)
admin.site.register(DatosPersona, DatosPersonaAdmin)
