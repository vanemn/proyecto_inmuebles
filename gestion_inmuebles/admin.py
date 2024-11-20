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
    list_display = (
        "comuna",
        "estado",
        "precio_min",
        "precio_max",
        "tipo_inmueble",
        "fecha_inicio",
        "fecha_fin",
        "nombre_autor",
        "titulo_autor",
    )
    search_fields = ("comuna__nombre", "estado", "nombre_autor")
    list_filter = (
        "estado",
        "tipo_inmueble",
        "dormitorios",
        "baños",
        "precio_min",
        "precio_max",
    )
