from functions.read_and_write import getJson, createNewJson, getLastUpdatedJson
from functions.data_generator import generar_votos, calcular_variacion_porcentajes


def main():
    print("############ SIMULADOR DE ELECCIONES ############")
  # ENTRADA

    jsonCandidates = getJson('../data/candidates.json') #JSON de candidatos --- OK
    lastUpdated = getLastUpdatedJson() # OBTIENE EL JSON CON EL PESO VIEJO --- OK
    updatedWeightJSON = calcular_variacion_porcentajes(lastUpdated) # == lastUpdated PROCESADO POR EL CODIGO DE MATI--- OK
    newJson = generar_votos(updatedWeightJSON, jsonCandidates) # --- Se produce excepcion por parametro de clave "poblacion"
    createNewJson(newJson)

  # PROCESAMIENTO
  # actualizar_json_candidatos(jsonWeight)

if __name__=="__main__":
  main()