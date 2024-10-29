# Función para obtener el partido de un candidato
def obtener_partido_candidato(jsonCandidates, candidato):
    try:
        # Obtiene el partido del candidato
        partido = jsonCandidates[candidato]["partido"]
        return partido
    except KeyError:
        return "Candidato no encontrado. Verifica el nombre del candidato."