from utils.data_storage import getJson


def main():
  print("############ SIMULADOR DE ELECCIONES ############")
  # ENTRADA

  muestra = getJson('../data/sample.json')
  muestra2 = getJson('../data/sample2.json')

  jsonCandidates = getJson('../data/candidates.json')

  for i in jsonCandidates:
    candidato = i
    partido = jsonCandidates[i]["partido"]
    print(f"{candidato} --> {partido}")

    #Prueba de json de Provincias
    print("\n############ POBLACION X PROVINCIA ############\n") 

    jsonProvincias = getJson('../data/provinces.json')
    for provincia in jsonProvincias:
        print(provincia + " --> " , jsonProvincias[provincia]["poblacion"])

if __name__=="__main__":
  main()
