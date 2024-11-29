import random 

def calcular_variacion_porcentajes(provinces_weight, variacion_maxima=5):
    porcentajes_ajustados = {}
    for provincia, datos in provinces_weight.items():
        porcentajes_ajustados[provincia] = {
            "peso": {},
            "poblacion": datos["poblacion"],
            "votos": datos["votos"],
            "votantes_ausentes": datos["votantes_ausentes"]
        }
        suma_ajustada = 0
        for candidato, base_porcentaje in datos["peso"].items():
            variacion = round(random.uniform(-variacion_maxima, variacion_maxima), 2)
            porcentaje_ajustado = round(base_porcentaje + variacion, 2)
            porcentaje_ajustado = max(min(porcentaje_ajustado, 100), 1)
            porcentajes_ajustados[provincia]["peso"][candidato] = porcentaje_ajustado
            suma_ajustada += porcentaje_ajustado
        diferencia = round(100.0 - suma_ajustada, 2)
        candidatos = list(porcentajes_ajustados[provincia]["peso"].keys())
        i = 0
        while diferencia != 0:
            candidato = candidatos[i % len(candidatos)]
            ajuste = 0.01 if diferencia > 0 else -0.01
            nuevo_valor = porcentajes_ajustados[provincia]["peso"][candidato] + ajuste
            if 1 <= nuevo_valor <= 100:
                porcentajes_ajustados[provincia]["peso"][candidato] = round(nuevo_valor, 2)
                diferencia = round(diferencia - ajuste, 2)
            i += 1
    return porcentajes_ajustados

def generar_votos(jsonMuestra, candidatos):
    candidates = list(candidatos.keys())
    for prov in jsonMuestra:
        padron = jsonMuestra[prov]["poblacion"] * 0.77
        poblacionVotanteAusente = padron * 0.23
        poblacionVotantePresente = padron - poblacionVotanteAusente
        for cand in candidates:
            candidateVotes = round((jsonMuestra[prov]["peso"][cand] * poblacionVotantePresente) / 100)
            jsonMuestra[prov]["votos"][cand] = candidateVotes
    return jsonMuestra