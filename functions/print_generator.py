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

    # # Obtener la ruta completa del directorio
    # script_dir = os.path.dirname(__file__)
    # full_path = os.path.join(script_dir, '../data/ddbb/', 'resultados.json')
    # os.makedirs(os.path.dirname(full_path), exist_ok=True)

    # # Leer el archivo existente si existe
    # if os.path.exists(full_path):
    #     with open(full_path, 'r') as file:
    #         try:
    #             informes = json.load(file)
    #         except json.JSONDecodeError:
    #             print("El archivo JSON de resultados no existe. Se creara un nuevo archivo de resultados.json")
    #             informes = []
    # else:
    #     informes = []

    # # Agregar los nuevos resultados a los informes existentes
    # informes.extend(resultados)

    # # Guardar los resultados en el archivo resultados.json
    # with open(full_path, 'w') as file:
    #     json.dump(informes, file, indent=4)
    return totalVotos