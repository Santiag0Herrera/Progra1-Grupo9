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
def porcentaje_candidatos(muestra):
  total_votos = 0
  porcentajes = []
  for i in muestra:
    total_votos += i
  
  for i in muestra:
    porcentajes.append(int((i/total_votos)*100))
  
  return porcentajes
  
# multiplicar ese porcentaje pero con el 100% real
# devolver la cantidad de votos que saco cada candidato

def calcular_votos_reales(porcentajes, poblacion_total):

  for i in range(len(porcentajes)):
    porcentaje_real = (porcentajes[i] * poblacion_total) / 100
    porcentajes[i] = int(porcentaje_real)
  
  return porcentajes