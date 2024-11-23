import pandas as pd
import json

# Ruta del archivo Excel
excel_path = r"D:\proyectos_django\regionesycomunas.xlsx"

# Leer el archivo Excel
df = pd.read_excel(excel_path)

# Imprimir los nombres de las columnas para verificación
print("Columnas del DataFrame:", df.columns)

# Inicializar listas para regiones y comunas
regiones = []
comunas = []

region_pk = 1
comuna_pk = 1

# Variables para seguir la región y provincia actuales
current_region = None
current_province = None

# Recorrer el DataFrame
for index, row in df.iterrows():
    region_name = row['Region']
    province_name = row['Provincia']
    comuna_name = row['Comuna']
    
    # Mensajes de depuración
    print(f"Procesando fila {index}: Región - {region_name}, Provincia - {province_name}, Comuna - {comuna_name}")

    # Actualizar la región actual si no está vacía
    if not pd.isna(region_name):
        current_region = region_name
        region_exists = any(region['fields']['nombre'] == current_region for region in regiones)
        if not region_exists:
            regiones.append({
                "model": "gestion_inmuebles.region",
                "pk": region_pk,
                "fields": {
                    "nombre": current_region
                }
            })
            region_pk += 1
    
    # Actualizar la provincia actual si no está vacía
    if not pd.isna(province_name):
        current_province = province_name
    
    # Añadir la comuna a la lista de comunas
    if not pd.isna(comuna_name):
        # Encontrar el pk de la región correspondiente
        region_pk_for_comuna = next(region['pk'] for region in regiones if region['fields']['nombre'] == current_region)
        comunas.append({
            "model": "gestion_inmuebles.comuna",
            "pk": comuna_pk,
            "fields": {
                "nombre": comuna_name,
                "region": region_pk_for_comuna
            }
        })
        comuna_pk += 1

# Unir regiones y comunas en un solo archivo de fixtures
fixtures = regiones + comunas

# Guardar el archivo JSON
with open('regiones_comunas.json', 'w', encoding='utf-8') as f:
    json.dump(fixtures, f, ensure_ascii=False, indent=4)

print("Archivo JSON de fixture creado con éxito.")
