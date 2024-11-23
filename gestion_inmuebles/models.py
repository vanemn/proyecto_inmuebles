from django.db import models
from django.utils import timezone


class Region(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,default=1)
    def __str__(self):
        return self.nombre


class Inmueble(models.Model):

    ESTADO_CHOICES = [
        ("reservada", "Reservada"),
        ("en_alquiler", "En Alquiler"),
    ]

    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=1)
    comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE, default=1)
    nombre = models.CharField(max_length=200)
    dormitorios = models.PositiveIntegerField(default=1)
    baños = models.PositiveIntegerField(default=1)
    estado = models.CharField(
        max_length=20, choices=ESTADO_CHOICES, default="en_alquiler"
    )
    precio_min = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    precio_max = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    tipo_inmueble = models.CharField(max_length=50)
    fecha_inicio = models.DateField(default=timezone.now)
    fecha_fin = models.DateField(default=timezone.now)
    imagen = models.ImageField(upload_to="imagenes_inmuebles/", null=True, blank=True)
    descripcion = models.TextField(max_length=250, default="", blank=True, null=True)
    m2_construidos = models.FloatField()
    m2_totales = models.FloatField()
    nombre_autor = models.CharField(max_length=100, default="Desconocido")
    titulo_autor = models.CharField(max_length=100, default="Desconocido")
    imagen_autor = models.ImageField(
        upload_to="imagenes_autores/", null=True, blank=True
    )
    estacionamientos = models.IntegerField(null=True, blank=True)
    precio_mensual = models.DecimalField(
        max_digits=10, decimal_places=0, null=True, blank=True
    )

    def __str__(self):
        return f"{self.comuna} - {self.estado}"
