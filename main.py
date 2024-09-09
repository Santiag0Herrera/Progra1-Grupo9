from utils.input_handler import ingresar_datos
from utils.data_generator import generar_muestra
from utils.data_storage import obtener_datos
from utils.calculation import poblacion_votante
from utils.calculation import porcentaje_candidatos
from utils.calculation import calcular_votos_reales

def main():
  print("############ SIMULADOR DE ELECCIONES ############")
  tamaño_muestra, candidatos, partidos = ingresar_datos()
  muestra = generar_muestra(tamaño_muestra, candidatos)
  provincias, poblacion = obtener_datos()
  votantes_X_Provincia, porcentaje_poblacion_votante = poblacion_votante(poblacion)
  resultados_muestra = porcentaje_candidatos(muestra)
  estimacion = calcular_votos_reales(muestra, 30000000)

  print(f"""
  +----------------------------------+
  |       RESULTADOS DE MUESTRA      |
  +----------------------------------+
  """)
  for i in range(len(candidatos)):
    for j in range(len(candidatos[i])):
      print(f"    {candidatos[i][j]}: {estimacion[i]} -- {resultados_muestra[i]}%")
  print("  +----------------------------------+")
  

if __name__=="__main__":
  main()