import random
from functions.data_weight import matrizPesoCandidatoxProvincia as matriz_pesos_original

# Función para aplicar variaciones del 5% a la matriz de pesos en porcentajes con decimales
def aplicar_variacion_matriz_pesos(matriz_pesos_original, variacion_maxima=5):
    nueva_matriz_pesos = [fila[:] for fila in matriz_pesos_original]  # Copiar la matriz original

    # Aplicar la variación del 5% (con hasta dos decimales) a cada peso
    for i in range(len(nueva_matriz_pesos)):
        total_original = sum(nueva_matriz_pesos[i])

        # Aplicar variación del 5% a cada peso individualmente
        for j in range(len(nueva_matriz_pesos[i])):
            # Variación aleatoria entre -5% y 5% con dos decimales
            variacion = round(random.uniform(-variacion_maxima, variacion_maxima), 2)
            nuevo_peso = nueva_matriz_pesos[i][j] + variacion

            # Asegurar que ningún peso sea menor a 1% y no mayor de 100%
            nueva_matriz_pesos[i][j] = round(max(min(nuevo_peso, 100), 1), 2) # Ajustar a 1% y 100%

        # Ajustar para que los pesos sumen exactamente 100% (o lo más cercano posible con dos decimales)
        total_ajustado = round(sum(nueva_matriz_pesos[i]), 2)  # Suma de los pesos ajustados

        if total_ajustado != 100.00: # Si la suma no es exactamente 100%
            diferencia = round(100.00 - total_ajustado, 2) # Diferencia entre 100% y la suma ajustada
            while diferencia != 0:
                # Aplicar corrección proporcionalmente sin afectar los pesos que ya son 1 o 100
                for j in range(len(nueva_matriz_pesos[i])): 
                    if diferencia == 0:
                        break

                    if diferencia > 0 and nueva_matriz_pesos[i][j] < 100: # Aumentar pesos menores a 100
                        nueva_matriz_pesos[i][j] = round(nueva_matriz_pesos[i][j] + 0.01, 2) # Aumentar 1%
                        diferencia = round(diferencia - 0.01, 2) # Reducir la diferencia
                    elif diferencia < 0 and nueva_matriz_pesos[i][j] > 1: # Reducir pesos mayores a 1
                        nueva_matriz_pesos[i][j] = round(nueva_matriz_pesos[i][j] - 0.01, 2) # Reducir 1%
                        diferencia = round(diferencia + 0.01, 2) # Aumentar la diferencia

    return nueva_matriz_pesos

# Generar la primera matriz de pesos con variación
matrizPesoEnero = aplicar_variacion_matriz_pesos(matriz_pesos_original)
matrizPesoFebrero = aplicar_variacion_matriz_pesos(matrizPesoEnero)
matrizPesoMarzo = aplicar_variacion_matriz_pesos(matrizPesoFebrero)
matrizPesoAbril = aplicar_variacion_matriz_pesos(matrizPesoMarzo)
matrizPesoMayo = aplicar_variacion_matriz_pesos(matrizPesoAbril)
matrizPesoJunio = aplicar_variacion_matriz_pesos(matrizPesoMayo)
matrizPesoJulio = aplicar_variacion_matriz_pesos(matrizPesoJunio)
matrizPesoAgosto = aplicar_variacion_matriz_pesos(matrizPesoJulio)
matrizPesoSeptiembre = aplicar_variacion_matriz_pesos(matrizPesoAgosto)
matrizPesoOctubre = aplicar_variacion_matriz_pesos(matrizPesoSeptiembre)  

# Imprimir la matriz con la variación del primer mes
print("Matriz de pesos de los partidos políticos en las provincias de Argentina (Enero):")
for fila in matrizPesoEnero:
    print(fila)
print ("\n")
# Imprimir la matriz con la variación del segundo mes
print("Matriz de pesos de los partidos políticos en las provincias de Argentina (Febrero):")
for fila in matrizPesoFebrero:
    print(fila)
print ("\n")
# Imprimir la matriz con la variación del tercer mes
print("Matriz de pesos de los partidos políticos en las provincias de Argentina (Marzo):")
for fila in matrizPesoMarzo:
    print(fila)
