import json

with open('C:/Users/Francisco/Desktop/Progra1-Grupo9-develop/data/candidates.json', 'r') as file:
    jsonCandidates = json.load(file)

# Función para obtener el partido de un candidato
def obtener_partido_candidato(jsonCandidates, candidato):
    try:
        # Obtiene el partido del candidato
        partido = jsonCandidates[candidato]["partido"]
        return partido
    except KeyError:
        return "Candidato no encontrado. Verifica el nombre del candidato."
    
#Ejemplo:
#Obtiene el partido de Javier Milei
partido = obtener_partido_candidato(jsonCandidates, "Javier Milei")
print("Partido de Javier Milei:", partido)
