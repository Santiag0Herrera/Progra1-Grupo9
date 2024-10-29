from functions.read_and_write import getJson, createNewJson, getLastUpdatedJson, saveJson
from functions.data_generator import generar_votos, calcular_variacion_porcentajes
from functions.print_generator import generar_salida


def main():
    print("############ SIMULADOR DE ELECCIONES ############")
    # ENRTADA
    jsonCandidates = getJson('../data/candidates.json') 

    # PROCESO
    lastUpdated = getLastUpdatedJson() 
    updatedWeightJSON = calcular_variacion_porcentajes(lastUpdated) 
    newJson = generar_votos(updatedWeightJSON, jsonCandidates) 
    createNewJson(newJson)
    

    # SALIDA
    generar_salida(newJson)

if __name__=="__main__":
  main()