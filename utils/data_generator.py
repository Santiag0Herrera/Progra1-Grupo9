import random 
import math

# Cálculo automático del tamaño de la muestra
def calcular_tamaño_muestra():
  # Solicitar solo el tamaño de la población
  N = int(input("Ingresa el tamaño de la población (N): "))
  while N <= 0:
      print("¡El tamaño de la población debe ser mayor a cero!")
      N = int(input("Ingresa el tamaño de la población (N): "))

  Nvotante = N*0.77 #Se asume que el 77% de la población es votante
 
  # Valores predeterminados
  Z = 1.96  # Z para 95% de nivel de confianza
  p = 0.5   # Proporción estimada de la población (0.5 es el más conservador)
  E = 0.05  # Margen de error (5%)

  # Cálculo del tamaño de la muestra sin corrección de población finita
  n = (Z*2 * p * (1 - p)) / (E*2) #Tamaño de la muestra sin corrección de población finita
  n_corrigido = n / (1 + ((n - 1) / Nvotante)) 
  return math.ceil(n_corrigido)

def generar_votos (candidatos):
    candidatosMuestra = []
    listaMuestra = []

    for i in candidatos:
        for j in i:
            candidatosMuestra.append(j)  
    
    for i in range (len(candidatosMuestra)):
        listaMuestra.append(0)
    
    for _ in range(calcular_tamaño_muestra()):
        candidatoIndice = random.randint(0, len(candidatosMuestra)-1)
        listaMuestra[candidatoIndice] = listaMuestra[candidatoIndice] + 1
        
    return listaMuestra





