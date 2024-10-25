from functions.read_and_write import getJson, createNewJson, getLastUpdatedJson
from functions.data_generator import generar_votos, calcular_variacion_porcentajes


def main():
  print("############ SIMULADOR DE ELECCIONES ############")
  # ENTRADA

  jsonCandidates = getJson('../data/candidates.json')
  lastUpdated = getLastUpdatedJson() # OBTIENE EL JSON CON EL PESO VIEJO
  updatedWeightJSON = calcular_variacion_porcentajes(lastUpdated) # == lastUpdated PROCESADO POR EL CODIGO DE MATI
  newJson = generar_votos(updatedWeightJSON, jsonCandidates)
  createNewJson(newJson)

  # PROCESAMIENTO
  # actualizar_json_candidatos(jsonWeight)

if __name__=="__main__":
  main()