def poblacion_votante(poblacion_total):
    poblacion_votante = []
    poblacion_votante_total = 0
    porcentaje_poblacion_votante = []
# Estimacion de el 77% de la población como votantes habilitados (mayores de 16 y menores de 80)
    for p in poblacion_total:
        estimacion_votantes = int(p * 0.77)
        poblacion_votante.append(estimacion_votantes)
        poblacion_votante_total += estimacion_votantes
    for i in poblacion_votante:
        porcentaje_poblacion_votante.append(str(int((i/poblacion_votante_total)*100)) + "%")
    return poblacion_votante, porcentaje_poblacion_votante

