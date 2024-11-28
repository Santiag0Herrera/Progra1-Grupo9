from functions.read_and_write import getJson, createNewJson, getLastUpdatedJson, createInforme
from functions.data_generator import generar_votos, calcular_variacion_porcentajes
from functions.print_generator import generar_salida, generar_tabla_porcentaje_candidato

def main():
    # ENRTADA
    jsonCandidates = getJson('../data/candidates.json') 

    # PROCESO
    lastUpdated = getLastUpdatedJson() 
    updatedWeightJSON = calcular_variacion_porcentajes(lastUpdated) 
    newJson = generar_votos(updatedWeightJSON, jsonCandidates)
    createNewJson(newJson)

    # SALIDA
    result = generar_salida(newJson)
    createInforme(result)
    generar_tabla_porcentaje_candidato(newJson)

if __name__=="__main__":
  main()