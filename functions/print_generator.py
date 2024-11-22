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

def generar_tabla_porcentaje_candidato(jsonFinal, csv_file = 'data/resultados.csv'):
    totalVotos = {}
    for prov in jsonFinal:
        for cand in jsonFinal[prov]["votos"]:
            if cand in totalVotos:
                totalVotos[cand] += jsonFinal[prov]["votos"][cand]
            else:
                totalVotos[cand] = jsonFinal[prov]["votos"][cand]
    
    total_votos_sum = sum(totalVotos.values())

    resultados = []
    for cand in totalVotos:
        resultados.append({
            "candidato": cand,
            "votos": totalVotos[cand],
            "porcentaje": round((totalVotos[cand] / total_votos_sum) * 100, 2)
        })

    existing_data = {}
    try:
        with open(csv_file, 'r') as f:
            lines = f.readlines()
            headers = lines[0].strip().split(', ')
            for line in lines[1:]:
                values = line.strip().split(', ')
                candidato = values[0]
                existing_data[candidato] = {headers[i]: values[i] for i in range(len(headers))}
    except FileNotFoundError:

        headers = ['Candidato']
        existing_data = {item['candidato']: {'Candidato': item['candidato']} for item in resultados}

    new_column_name = f"{len(headers) - 1}"
    headers.append(new_column_name)
    for item in resultados:
        candidato = item['candidato']
        if candidato in existing_data:
            existing_data[candidato][new_column_name] = str(item['porcentaje'])
        else:
            existing_data[candidato] = {'Candidato': candidato, new_column_name: str(item['votos'])}
    
    with open(csv_file, 'w') as f:
        f.write(', '.join(headers) + '\n')
        for row in existing_data.values():
            f.write(', '.join(row.get(header, '') for header in headers) + '\n')
    

def generar_tabla_porcentaje_provincia(jsonFinal, csv_file='data/resultados_provincias.csv'):
    resultados = {}
    for prov in jsonFinal:
        total_votos_provincia = sum(jsonFinal[prov]["votos"].values())
        resultados[prov] = {}
        for cand, votos in jsonFinal[prov]["votos"].items():
            resultados[prov][cand] = round((votos / total_votos_provincia) * 100, 2)
    existing_data = {}
    headers = ['Provincia']
    try:
        with open(csv_file, 'r') as f:
            lines = f.readlines()
            headers = lines[0].strip().split(', ')
            for line in lines[1:]:
                values = line.strip().split(', ')
                provincia = values[0]
                existing_data[provincia] = {headers[i]: values[i] for i in range(len(headers))}
    except FileNotFoundError:
        existing_data = {prov: {'Provincia': prov} for prov in resultados}

    for prov, data in resultados.items():
        if prov not in existing_data:
            existing_data[prov] = {'Provincia': prov}
        for cand, porcentaje in data.items():
            if cand not in headers:
                headers.append(cand)
            existing_data[prov][cand] = str(porcentaje)
    
    with open(csv_file, 'w') as f:
        f.write(', '.join(headers) + '\n')
        for row in existing_data.values():
            f.write(', '.join(row.get(header, '') for header in headers) + '\n')