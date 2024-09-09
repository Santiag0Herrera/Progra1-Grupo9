from utils.input_handler import ingresar_datos
from utils.data_generator import generar_muestra

def main():
  print("############ SIMULADOR DE ELECCIONES ############")
  tamaño_muestra, candidatos, partidos = ingresar_datos()
  
  muestra = generar_muestra(tamaño_muestra, candidatos)
  
  print(f"""
  +----------------------------------+
  |       CANDIDATOS X PARTIDO       |
  +----------------------------------+
  """)
  for i in range(len(partidos)):
    print(f"  {partidos[i]}")
    for j in range(len(candidatos[i])):
      print(f"    - {candidatos[i][j]}") 
  print("+----------------------------------+")
  

if __name__=="__main__":
  main()