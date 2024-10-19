import random 
import math

# Cálculo automático del tamanio de la muestra
def calcular_tamanio_muestra():
  # Solicitar solo el tamanio de la población
  N = int(input("Ingresa el tamanio de la población (N): "))
  while N <= 0:
      print("¡El tamanio de la población debe ser mayor a cero!")
      N = int(input("Ingresa el tamanio de la población (N): "))

  Nvotante = N*0.77 #Se asume que el 77% de la población es votante
 
  # Valores predeterminados
  Z = 1.96  # Z para 95% de nivel de confianza
  p = 0.5   # Proporción estimada de la población (0.5 es el más conservador)
  E = 0.05  # Margen de error (5%)

  # Cálculo del tamanio de la muestra sin corrección de población finita
  n = (Z**2 * p * (1 - p)) / (E**2) #Tamanio de la muestra sin corrección de población finita
  n_corrigido = n / (1 + ((n - 1) / Nvotante)) 
  return math.ceil(n_corrigido), Nvotante

def generar_votos (candidatos):
    candidatosMuestra = []
    listaMuestra = []

    for i in candidatos:
        for j in i:
            candidatosMuestra.append(j) # => podemos agregar aca el listaMuestra.append(0)
    
    for i in range (len(candidatosMuestra)):
        listaMuestra.append(0)
    
    tamanio_de_muestra, total_votantes_reales = calcular_tamanio_muestra()

    for _ in range(tamanio_de_muestra):
        candidatoIndice = random.randint(0, len(candidatosMuestra)-1)
        listaMuestra[candidatoIndice] = listaMuestra[candidatoIndice] + 1
        
    return candidatosMuestra, listaMuestra, total_votantes_reales





