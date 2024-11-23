import os
import sys
import django

# Configurar el entorno de Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmuebles.settings')
django.setup()

from gestion_inmuebles.models import Inmueble

def consultar_inmuebles_comunas():
    inmuebles = Inmueble.objects.filter(estado='en_alquiler').values('comuna__nombre', 'nombre', 'descripcion')
    resultado = {}

    for inmueble in inmuebles:
        comuna = inmueble['comuna__nombre']
        if comuna not in resultado:
            resultado[comuna] = []
        resultado[comuna].append(f"Nombre: {inmueble['nombre']}, Descripción: {inmueble['descripcion']}")

    with open('inmuebles_por_comunas.txt', 'w') as file:
        for comuna, inmuebles in resultado.items():
            file.write(f"Comuna: {comuna}\n")
            for detalle in inmuebles:
                file.write(f"  {detalle}\n")
            file.write("\n")

if __name__ == "__main__":
    consultar_inmuebles_comunas()
