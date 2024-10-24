from functions.read_and_write import getJson, createNewJson, getLastUpdatedJson
from functions.time_line_candidates import actualizar_json_candidatos


def main():
  print("############ SIMULADOR DE ELECCIONES ############")
  # ENTRADA

  jsonCandidates = getJson('../data/candidates.json')
  jsonWeight = getJson('../data/provinces_weight.json')
  print(getLastUpdatedJson())
  newJson = {"matias": "chau"}
  createNewJson(newJson)


  # PROCESAMIENTO
  # actualizar_json_candidatos(jsonWeight)

if __name__=="__main__":
  main()
