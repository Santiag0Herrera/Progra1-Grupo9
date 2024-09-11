from utils.input_handler import ingresar_datos
from utils.data_generator import generar_votos
from utils.calculation import porcentaje_candidatos
from utils.calculation import calcular_votos_reales
from utils.print_generator import generar_salida

def main():
  print("############ SIMULADOR DE ELECCIONES ############")
  # ENTRADA
  candidatos, partidos = ingresar_datos()

  # PROCESO
  candidatosMuestra, votosMuestra, total_votantes_reales = generar_votos(candidatos)
  porcentajes = porcentaje_candidatos(votosMuestra)
  estimacion = calcular_votos_reales(porcentajes, total_votantes_reales)

  # SALIDA
  generar_salida(total_votantes_reales, porcentajes, candidatosMuestra, estimacion)

if __name__=="__main__":
  main()  