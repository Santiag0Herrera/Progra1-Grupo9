from utils.data_storage import getJson


def main():
  print("############ SIMULADOR DE ELECCIONES ############")
  # ENTRADA

  jsonCandidates = getJson('../data/candidates.json')

  for i in jsonCandidates:
    candidato = i
    partido = jsonCandidates[i]["partido"]
    print(f"{candidato} --> {partido}")

    #Prueba de json de Provincias
    print("\n############ POBLACION X PROVINCIA ############\n") # Added a newline character

    jsonProvincias = getJson('../data/provinces.json')
    for provincia in jsonProvincias:
        print(provincia + " --> " , jsonProvincias[provincia]["poblacion"])

if __name__=="__main__":
  main()
