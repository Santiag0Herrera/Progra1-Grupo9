import math
from utils.provinces import jsonProvinces

# Función para calcular la población total
def calcular_poblacion_total(jsonProvinces):
    poblacion_total = 0
    for provincia in jsonProvinces.values():
        poblacion_total += provincia["población"]
    return poblacion_total

# Función para calcular el tamaño de la muestra
def calcular_tamanio_muestra(jsonProvinces):
    # Llamamos a la función que calcula la población total
    N = calcular_poblacion_total(jsonProvinces)
    
    Nvotante = N * 0.77  # Se asume que el 77% de la población es votante
    
    # Valores predeterminados
    Z = 1.96  # Z para 95% de nivel de confianza
    p = 0.5   # Proporción estimada de la población (0.5 es el más conservador)
    E = 0.05  # Margen de error (5%)

    # Cálculo del tamaño de la muestra sin corrección de población finita
    n = (Z**2 * p * (1 - p)) / (E**2)  # Tamaño de la muestra sin corrección
    n_corrigido = n / (1 + ((n - 1) / Nvotante)) 
    
    return math.ceil(n_corrigido), Nvotante

# Ejemplo de cálculo
poblacion_total = calcular_poblacion_total(jsonProvinces)
muestra, votantes = calcular_tamanio_muestra(jsonProvinces)

print(f"Población total: {poblacion_total}")
print(f"Votantes estimados: {votantes}")
print(f"Tamaño de la muestra requerida: {muestra}")