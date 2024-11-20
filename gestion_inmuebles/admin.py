from django.contrib import admin
from .models import Region, Comuna, Inmueble


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    search_fields = ("nombre",)


@admin.register(Inmueble)
class InmuebleAdmin(admin.ModelAdmin):
    #para definir columnas a mostrar
    list_display = (
        "region",
        "comuna",
        "estado",
        "precio_min",
        "precio_max",
        "tipo_inmueble",
        "fecha_inicio",
        "fecha_fin",
    )
    
    #para añadir a la barra de busqueda
    search_fields = ("comuna__nombre", "estado", "tipo_inmueble")

    #para añadir filtros
    list_filter = (
        "region",
        "dormitorios",
        "estado",
        "comuna",
        "tipo_inmueble",
    )
