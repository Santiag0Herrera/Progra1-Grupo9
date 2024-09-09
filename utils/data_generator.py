import random 

#teniendo el tamaño de muestra que se ingresa por teclado tengo que asignarle un candidato a cada persona de la muestra y eso guardarlo en una lista hermanada a la lista de
#candidatos
listaMuestra = []

def generar_muestra(tamaño_muestra, partidos, candidatos):
    for _ in range(tamaño_muestra):
        partido = random.choice(partidos)
        candidato = random.choice(candidatos[partidos.index(partido)])
        listaMuestra.append([partido, candidato])
    return listaMuestra


