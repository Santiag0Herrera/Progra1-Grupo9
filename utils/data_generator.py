import random 

#teniendo el tamaño de muestra que se ingresa por teclado tengo que asignarle un candidato a cada persona de la muestra y eso guardarlo en una lista hermanada a la lista de
#candidatos

def generar_muestra(tamaño_muestra, candidatos):
    candidatosMuestra = []
    listaMuestra = []

    for i in candidatos:
        for j in i:
            candidatosMuestra.append(j)  
    
    for i in range (len(candidatosMuestra)):
        listaMuestra.append(0)
    
    for _ in range(tamaño_muestra):
        candidatoIndice = random.randint(0, len(candidatosMuestra)-1)
        listaMuestra[candidatoIndice] = listaMuestra[candidatoIndice] + 1
        
    return listaMuestra




