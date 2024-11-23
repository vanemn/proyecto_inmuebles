import os
import sys
import django
from django.db import connection

# Configurar el entorno de Django
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto_inmuebles.settings')
django.setup()

def consultar_inmuebles_regiones_sql():
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT region.nombre, inmueble.nombre, inmueble.descripcion
            FROM gestion_inmuebles_inmueble as inmueble
            JOIN gestion_inmuebles_region as region ON inmueble.region_id = region.id
            WHERE inmueble.estado = 'en_alquiler'
        """)
        inmuebles = cursor.fetchall()

    resultado = {}
    for inmueble in inmuebles:
        region, nombre, descripcion = inmueble
        if region not in resultado:
            resultado[region] = []
        resultado[region].append(f"Nombre: {nombre}, Descripción: {descripcion}")

    with open('inmuebles_por_regiones_sql.txt', 'w') as file:
        for region, inmuebles in resultado.items():
            file.write(f"Región: {region}\n")
            for detalle in inmuebles:
                file.write(f"  {detalle}\n")
            file.write("\n")

if __name__ == "__main__":
    consultar_inmuebles_regiones_sql()
