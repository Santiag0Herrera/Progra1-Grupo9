import json
import os

def generar_salida(jsonFinal):
    print("+------------------------------------------------------+")
    print("|                RESULTADOS DE REALES                  |")
    print("+------------------------------------------------------+")
    totalVotos = {}
    for prov in jsonFinal:
        for cand in jsonFinal[prov]["votos"]:
            if cand in totalVotos:
                totalVotos[cand] += jsonFinal[prov]["votos"][cand]
            else:
                totalVotos[cand] = jsonFinal[prov]["votos"][cand]
    
    #total de votos
    total_votos_sum = sum(totalVotos.values())
    
    #Encabezado
    print("| " + ("Candidato" + " |" + "Votos".center(9) + "| " + "Porcentaje").center(52) + " |")
    print("+------------------------------------------------------+")

    # Filas
    resultados = []
    for cand in totalVotos:
        candidato = cand.center(20)
        votos = str(totalVotos[cand]).center(10)
        porcentaje = f"{round((totalVotos[cand] / total_votos_sum) * 100, 2)}%".center(10)
        print(f"{candidato} | {votos} | {porcentaje}")
        resultados.append({
            "candidato": cand,
            "votos": totalVotos[cand],
            "porcentaje": round((totalVotos[cand] / total_votos_sum) * 100, 2)
        })
    print("+------------------------------------------------------+")

    return totalVotos