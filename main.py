from utils.input_handler import ingresar_datos
from utils.data_generator import generar_muestra
from utils.data_storage import obtener_datos
from utils.calculation import poblacion_votante

def main():
  print("############ SIMULADOR DE ELECCIONES ############")
  tamaño_muestra, candidatos, partidos = ingresar_datos()
  
  muestra = generar_muestra(tamaño_muestra, candidatos)
  provincias, poblacion = obtener_datos()
  votantes_X_Provincia,porcentaje_poblacion_votante = poblacion_votante(poblacion)
  print(f"POBLACION HABILITADA A VOTAR: {votantes_X_Provincia} \n PORCENTAJE: {porcentaje_poblacion_votante}")
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