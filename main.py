from utils.input_handler import ingresar_datos
from utils.data_generator import generar_votos
from utils.data_storage import obtener_datos
from utils.calculation import poblacion_votante
from utils.calculation import porcentaje_candidatos
from utils.calculation import calcular_votos_reales
from utils.calculation import calcular_balotaje


def main():
  print("############ SIMULADOR DE ELECCIONES ############")
  candidatos, partidos = ingresar_datos()
  muestra = generar_votos(candidatos)
  print(muestra)
  provincias, poblacion = obtener_datos()
  votantes_X_Provincia, porcentaje_poblacion_votante = poblacion_votante(poblacion)
  resultados_muestra = porcentaje_candidatos(muestra)
  estimacion = calcular_votos_reales(muestra, 30000000)
  ganadores, habra_balotaje = calcular_balotaje(resultados_muestra, candidatos)

  
  
  print("+----------------------------------+")
  print("|       RESULTADOS DE MUESTRA      |")
  print("+----------------------------------+")
  for i in range(len(candidatos)):
    for j in range(len(candidatos[i])):
      print(f"    {candidatos[i][j]}: {estimacion[i]} -- {resultados_muestra[i]}%")
  print("  +----------------------------------+")

  if habra_balotaje:
    print("|       RESULTADOS DE BALOTAJE     |")
    print("+----------------------------------+")
    print(f"  HAY BALOTAJE ENTRE: {ganadores[0]} y {ganadores[1]}.")
  else:
    print("|       RESULTADOS FINALES         |")
    print("+----------------------------------+")
    print(f"  HAY MAS DEL 50% DE LOS VOTOS PARA UN CANDIDATO. NO HAY BALOTAJE.")
    print(f"  EL GANADOR ES: {ganadores[0]}.")

  print("  +----------------------------------+")

if __name__=="__main__":
  main()  