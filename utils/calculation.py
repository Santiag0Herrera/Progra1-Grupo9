def poblacion_votante(poblacion_total):
    poblacion_votante = []
    poblacion_votante_total = 0
    porcentaje_poblacion_votante = []
    # Estimacion de el 77% de la población como votantes habilitados (mayores de 16 y menores de 80)
    for p in poblacion_total:
        estimacion_votantes = int(p * 0.77)
        poblacion_votante.append(estimacion_votantes)
        poblacion_votante_total += estimacion_votantes
        
    for i in poblacion_votante:
        porcentaje_poblacion_votante.append(str(int((i/poblacion_votante_total)*100)) + "%")
    return poblacion_votante, porcentaje_poblacion_votante

# sacar porcentaje de votos de muestra por cada candidato
def porcentaje_candidatos(lista_votos):
  total_votos = sum(lista_votos)
  porcentajes = []
  for i in range(len(lista_votos)):
    porcentaje = (lista_votos[i] / total_votos) * 100
    porcentajes.append(porcentaje)
  return porcentajes

# multiplicar ese porcentaje pero con el 100% real
# devolver la cantidad de votos que saco cada candidato

def calcular_votos_reales(porcentajes, poblacion_total):
  votos_reales = []
  porcentajes_reales = []

  for i in range(len(porcentajes)):
    voto_real = (porcentajes[i] * poblacion_total) / 100
    votos_reales.append(voto_real)
  
  total_votos_reals = sum(votos_reales)
  for i in range(len(votos_reales)):
    porcentaje_real = (votos_reales[i] / total_votos_reals) * 100
    porcentajes_reales.append(porcentaje_real)
  return votos_reales, porcentajes_reales

def calcular_balotaje(resultados_muestra, lista_candidatos):
    total_votos = sum(resultados_muestra)
    for i in range(len(resultados_muestra)):
        resultados_muestra[i] = int((resultados_muestra[i] / total_votos) * 100)

    for i in range(len(resultados_muestra)):
        if resultados_muestra[i] > 45:
            return [lista_candidatos[i]], False 
    
    max1, max2 = -1, -1  
    for i in range(len(resultados_muestra)):
        if max1 == -1 or resultados_muestra[i] > resultados_muestra[max1]:
            max2 = max1  
            max1 = i     
        elif max2 == -1 or resultados_muestra[i] > resultados_muestra[max2]:
            max2 = i     
    
    return [lista_candidatos[max1], lista_candidatos[max2]], True




