import random 

#teniendo el tamaño de muestra que se ingresa por teclado tengo que asignarle un candidato a cada persona de la muestra y eso guardarlo en una lista hermanada a la lista de
#candidatos

def generar_muestra(tamaño_muestra, candidatos):
    listaMuestra = []
    
    for i in range (len(candidatos)):
        listaMuestra.append(0)
    
    for _ in range(tamaño_muestra):
        candidatoIndice = random.randint(0, len(candidatos)-1)
        listaMuestra[candidatoIndice] = listaMuestra[candidatoIndice] + 1
        
    return listaMuestra




