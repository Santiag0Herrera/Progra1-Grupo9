def actualizar_json_candidatos(json_anterior):
  provinces = json_anterior
  for prov in provinces:
    # print(prov)
    print(json_anterior[prov]["peso"])