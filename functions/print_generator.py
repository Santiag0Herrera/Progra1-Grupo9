def generar_salida(total_votantes_reales, porcentajes_reales, candidatosMuestra, estimacion):
  print("+------------------------------------------------------+")
  print("|                RESULTADOS DE REALES                  |")
  print("+------------------------------------------------------+")
  mesnaje_votantes = f"Total de votantes: {total_votantes_reales}"
  print(f"|{mesnaje_votantes.center(54, ' ')}|")
  print("+------------------------------------------------------+")  
  for i in range(len(porcentajes_reales)):
      porcentaje_redondeado = round(porcentajes_reales[i], 2)
      mensaje = f"{candidatosMuestra[i]} {porcentaje_redondeado}% con {estimacion[i]} votos"
      print(f"|{mensaje.center(54, ' ')}|")
  print("+------------------------------------------------------+")