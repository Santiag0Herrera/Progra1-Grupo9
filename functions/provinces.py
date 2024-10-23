import json

# Cargar el archivo JSON
with open('C:/Users/Francisco/Desktop/Progra1-Grupo9-develop/data/provinces.json', 'r') as file:
    jsonProvinces = json.load(file)

# Obtener la población de una provincia
def buscar_poblacion(provincia):
    if provincia in jsonProvinces:
        return jsonProvinces[provincia]["población"]
    else:
        return f'La provincia "{provincia}" no se encuentra en el registro.'

# Ejemplo:
print(buscar_poblacion("Córdoba"))  # Devuelve 3978984
print(buscar_poblacion("Buenos Aires"))  # Devuelve 17569053
print(buscar_poblacion("Washington"))  # Devuelve mensaje de error