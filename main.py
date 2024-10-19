from utils.data_storage import getJson


def main():
  print("############ SIMULADOR DE ELECCIONES ############")
  # ENTRADA

  jsonCandidates = getJson('../data/candidates.json')

  for i in jsonCandidates:
    candidato = i
    partido = jsonCandidates[i]["partido"]
    print(f"{candidato} --> {partido}")

if __name__=="__main__":
  main()
