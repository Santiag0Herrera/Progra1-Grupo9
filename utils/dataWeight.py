# MATRIZ DE PESO DE LOS PARTIDOS POLÍTICOS EN LAS PROVINCIAS DE ARGENTINA

matrizPesoCandidatoxProvincia = [
    # Sergio Massa, Javier Milei, Patricia Bullrich, Juan Schiaretti, Mirian Bregman, Blanco/Nulos
    [42.95, 25.73, 24.05, 3.70, 3.57, 3.34],   # Buenos Aires
    [32.18, 19.98, 41.23, 3.97, 3.53, 2.50],   # Ciudad Autónoma de Buenos Aires
    [42.83, 32.03, 17.13, 6.44, 1.58, 7.80],  # Catamarca
    [43.67, 27.82, 24.10, 3.62, 0.78, 1.64],  # Chaco
    [32.22, 35.13, 20.57, 7.70, 4.38, 2.85],  # Chubut
    [13.42, 33.58, 22.63, 28.98, 1.39, 1.62], # Córdoba
    [37.21, 26.87, 32.13, 2.73, 1.06, 2.49],  # Corrientes
    [33.31, 29.74, 30.03, 5.36, 1.56, 5.53],  # Entre Ríos
    [52.31, 29.06, 15.38, 2.44, 0.81, 1.88],  # Formosa
    [32.36, 37.35, 19.96, 6.79, 3.54, 2.40],  # Jujuy
    [34.86, 33.51, 21.90, 7.44, 2.29, 1.83],  # La Pampa
    [41.14, 37.63, 11.80, 8.51, 0.92, 2.26],  # La Rioja
    [24.01, 42.38, 25.82, 4.32, 3.47, 3.03],  # Mendoza
    [37.93, 42.19, 14.39, 4.10, 1.40, 3.30],  # Misiones
    [31.76, 36.74, 20.56, 5.95, 4.99, 4.35],  # Neuquén
    [37.85, 33.76, 18.13, 6.25, 4.01, 4.41],  # Río Negro
    [38.00, 40.27, 13.80, 6.18, 1.75, 3.07],  # Salta
    [33.30, 35.08, 23.20, 6.17, 2.23, 2.46],  # San Juan
    [27.33, 43.33, 20.91, 6.24, 2.19, 2.99],  # San Luis
    [37.79, 36.30, 16.41, 6.60, 2.90, 7.79],  # Santa Cruz
    [29.70, 32.52, 26.88, 9.02, 1.89, 2.13],  # Santa Fe
    [65.77, 22.84, 8.01, 2.13, 1.25, 2.06],   # Santiago del Estero
    [38.20, 33.82, 14.99, 9.12, 3.86, 3.05],  # Tierra del Fuego
    [44.93, 35.00, 14.64, 3.99, 1.44, 3.19],  # Tucumán
    [32.18, 19.98, 41.23, 3.97, 3.53, 2.50]   # Ciudad Autónoma de Buenos Aires
]
# Función para obtener el peso de un partido en una provincia específica
def obtener_peso_partido_en_provincia(matriz, provincia_idx, partido_idx):
    """
    Obtiene el peso de un partido en una provincia específica.

    :param matriz: Matriz de datos con los resultados de las provincias.
    :param provincia_idx: Índice de la provincia en la matriz.
    :param partido_idx: Índice del partido en la matriz.
    :return: Peso del partido en la provincia especificada.
    """
    try:
        # Obtiene el peso del partido en la provincia
        peso = matriz[provincia_idx][partido_idx]
        return peso
    except IndexError:
        return "Índice fuera de rango. Verifica los índices de la provincia o del partido."


#Ejemplo:
#Obtiene el peso del partido de Sergio Massa en la provincia de Buenos Aires
peso = obtener_peso_partido_en_provincia(matrizPesoCandidatoxProvincia, 23, 0)
print("Peso de Sergio Massa en Buenos Aires:", peso)