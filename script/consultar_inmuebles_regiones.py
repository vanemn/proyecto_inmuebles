import os
import sys
import django

# Configurar el entorno de Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmuebles.settings')
django.setup()

from gestion_inmuebles.models import Inmueble

def consultar_inmuebles_regiones():
    inmuebles = Inmueble.objects.filter(estado='en_alquiler').values('region__nombre', 'nombre', 'descripcion')
    resultado = {}

    for inmueble in inmuebles:
        region = inmueble['region__nombre']
        if region not in resultado:
            resultado[region] = []
        resultado[region].append(f"Nombre: {inmueble['nombre']}, Descripción: {inmueble['descripcion']}")

    with open('inmuebles_por_regiones.txt', 'w') as file:
        for region, inmuebles in resultado.items():
            file.write(f"Región: {region}\n")
            for detalle in inmuebles:
                file.write(f"  {detalle}\n")
            file.write("\n")

if __name__ == "__main__":
    consultar_inmuebles_regiones()
