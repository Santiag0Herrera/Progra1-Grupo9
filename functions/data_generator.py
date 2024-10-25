import random 

def generar_votos (jsonMuestra, candidatos):
  candidates = list(candidatos.keys())

  for prov in jsonMuestra:
    padron = jsonMuestra[prov]["poblacion"]*0.77
    poblacionVotanteAusente = padron*0.3
    poblacionVotantePresente = padron - poblacionVotanteAusente

    for cand in candidates:
      jsonMuestra[prov]["votos"][cand] = (jsonMuestra[prov]["peso"][cand] * poblacionVotantePresente) / 100

  return jsonMuestra

def calcular_variacion_porcentajes(provinces_weight, variacion_maxima=5):
    # Diccionario para almacenar los porcentajes ajustados
    porcentajes_ajustados = {}

    # Procesar cada provincia en el JSON
    for provincia, datos in provinces_weight.items():
        porcentajes_ajustados[provincia] = {}
        
        # Suma para ajustar posteriormente a 100%
        suma_ajustada = 0

        for candidato, base_porcentaje in datos["peso"].items():
            # Variación aleatoria entre -5% y 5% con dos decimales
            variacion = round(random.uniform(-variacion_maxima, variacion_maxima), 2)
            porcentaje_ajustado = round(base_porcentaje + variacion, 2)
            
            # Limitar el porcentaje ajustado entre 1 y 100
            porcentaje_ajustado = max(min(porcentaje_ajustado, 100), 1)
            
            # Añadir al diccionario y acumular la suma para el ajuste final
            porcentajes_ajustados[provincia][candidato] = porcentaje_ajustado
            suma_ajustada += porcentaje_ajustado
        
        # Ajuste para que la suma sea exactamente 100%
        diferencia = round(100.0 - suma_ajustada, 2)
        
        # Si la diferencia es distinta de cero, corregir proporcionalmente
        candidatos = list(porcentajes_ajustados[provincia].keys())
        i = 0
        while diferencia != 0:
            candidato = candidatos[i % len(candidatos)]
            ajuste = 0.01 if diferencia > 0 else -0.01
            nuevo_valor = porcentajes_ajustados[provincia][candidato] + ajuste
            
            # Aplicar ajuste sin exceder los límites de 1% a 100%
            if 1 <= nuevo_valor <= 100:
                porcentajes_ajustados[provincia][candidato] = round(nuevo_valor, 2)
                diferencia = round(diferencia - ajuste, 2)
            i += 1
    
    return porcentajes_ajustados