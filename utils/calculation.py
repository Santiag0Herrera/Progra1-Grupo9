def porcentaje_candidatos(lista_votos):
  total_votos = sum(lista_votos)
  porcentajes = []
  for i in range(len(lista_votos)):
    porcentaje = (lista_votos[i] / total_votos) * 100
    porcentajes.append(porcentaje)
  return porcentajes


def calcular_votos_reales(porcentajes, poblacion_total):
  votos_reales = []
  for i in range(len(porcentajes)):
    voto_real = (porcentajes[i] * poblacion_total) / 100
    votos_reales.append(int(voto_real))
  return votos_reales