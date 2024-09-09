from utils.input_handler import ingresar_datos
from utils.data_generator import generar_datos_mustra
import utils.entrada as entrada

def main():
  entrada.entradaDeDatos()
  print("############ SIMULADOR DE ELECCIONES ############")
  tamaño_muestra, candidatos, partidos = ingresar_datos()

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
  
  generar_datos_mustra(tamaño_muestra, candidatos, partidos)
  

if __name__=="__main__":
  main()