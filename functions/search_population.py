# Obtener la población de una provincia
def buscar_poblacion(provincia, jsonProvinces):
    if provincia in jsonProvinces:
        return jsonProvinces[provincia]["población"]
    else:
        return f'La provincia "{provincia}" no se encuentra en el registro.'