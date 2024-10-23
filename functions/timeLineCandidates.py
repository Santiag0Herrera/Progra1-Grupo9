from variationWeight import matrizPesoEnero, matrizPesoFebrero, matrizPesoMarzo, matrizPesoAbril, matrizPesoMayo, matrizPesoJunio, matrizPesoJulio, matrizPesoAgosto, matrizPesoSeptiembre, matrizPesoOctubre

def crearMatrizCandidato(matrizPesoEnero, matrizPesoFebrero, matrizPesoMarzo, matrizPesoAbril, matrizPesoMayo, matrizPesoJunio, matrizPesoJulio, matrizPesoAgosto, matrizPesoSeptiembre, matrizPesoOctubre):
    num_provincias = len(matrizPesoEnero)  # Obtener el número de provincias

    # Crear una matriz vacía para almacenar los pesos del candidato en cada provincia por mes
    matrizCandidato = [[0] * 10 for _ in range(num_provincias)]  # 10 columnas para enero a agosto

    # Llenar la matriz con los pesos del candidato
    for provincia in range(num_provincias):
        matrizCandidato[provincia][0] = matrizPesoEnero[provincia][0]    # Enero
        matrizCandidato[provincia][1] = matrizPesoFebrero[provincia][0]  # Febrero
        matrizCandidato[provincia][2] = matrizPesoMarzo[provincia][0]    # Marzo
        matrizCandidato[provincia][3] = matrizPesoAbril[provincia][0]    # Abril
        matrizCandidato[provincia][4] = matrizPesoMayo[provincia][0]     # Mayo
        matrizCandidato[provincia][5] = matrizPesoJunio[provincia][0]    # Junio
        matrizCandidato[provincia][6] = matrizPesoJulio[provincia][0]    # Julio
        matrizCandidato[provincia][7] = matrizPesoAgosto[provincia][0]   # Agosto
        matrizCandidato[provincia][8] = matrizPesoSeptiembre[provincia][0]  # Septiembre
        matrizCandidato[provincia][9] = matrizPesoOctubre[provincia][0]     # Octubre

    return matrizCandidato

# Llamar a la función con todas las matrices de pesos de enero a agosto
matrizCandidato = crearMatrizCandidato(
    matrizPesoEnero, matrizPesoFebrero, matrizPesoMarzo, 
    matrizPesoAbril, matrizPesoMayo, matrizPesoJunio, 
    matrizPesoJulio, matrizPesoAgosto, matrizPesoSeptiembre, matrizPesoOctubre
)

# Imprimir la matriz del candidato para verificar
print ("Matriz de pesos del candidato en las provincias de Argentina:")
for fila in matrizCandidato:
    print(fila)
