from functions.read_and_write import verify_if_exists_csv, create_new_empty_csv, write_csv, read_new_csv

def sumar_votos_candidatos_recursiva(province_list, candidates_result=None):
    if candidates_result is None:
        candidates_result = {}

    if len(province_list) == 0:
        return candidates_result
    else:
        province_key, province_value = province_list.popitem()
        for cand in province_value["votos"]:
            if cand in candidates_result:
                candidates_result[cand] += province_value["votos"][cand]
            else:
                candidates_result[cand] = province_value["votos"][cand]
        return sumar_votos_candidatos_recursiva(province_list, candidates_result)

def generar_salida(jsonFinal):
  totalVotos = sumar_votos_candidatos_recursiva(jsonFinal.copy())
  return totalVotos

def generar_tabla_porcentaje_candidato(jsonFinal, csv_file = 'resultados.csv'):
  totalVotos = sumar_votos_candidatos_recursiva(jsonFinal.copy())
  total_votos_sum = sum(totalVotos.values())
  csv_content = ""

  if verify_if_exists_csv(csv_file) == False:
      create_new_empty_csv(csv_file)
      for cand in totalVotos:
        porcentaje = f"{round((totalVotos[cand] / total_votos_sum) * 100, 2)}%"
        csv_content += f"{cand}, {porcentaje}\n"
  else: 
    csv_content = read_new_csv(csv_file)
    for cand in totalVotos:
        porcentaje = f"{round((totalVotos[cand] / total_votos_sum) * 100, 2)}%"
        lines = csv_content.split('\n')
        for i, line in enumerate(lines):
            if cand in line:
                lines[i] += f", {porcentaje}"
        csv_content = '\n'.join(lines)

  write_csv(csv_file, csv_content)


def generar_tabla_porcentaje_provincia(jsonFinal, candidates, csv_file='resultados_provincias.csv'):
  csv_content = " ,"
  for candidate in candidates:
    csv_content += f'{candidate}, '

  csv_content += '\n'
  for province in jsonFinal:
    csv_content += f"{province}, "
    for candidate in candidates:
      if candidate in jsonFinal[province]["peso"]:
        csv_content += f"{round(jsonFinal[province]['peso'][candidate], 2)}%, "
    csv_content += '\n'

  if verify_if_exists_csv(csv_file) == False:
    create_new_empty_csv(csv_file)
  write_csv(csv_file, csv_content)
