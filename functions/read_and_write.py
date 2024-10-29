import json
import os
from functions.backup import backupJson0

def getJson(fileName):
    # Obtener la ruta del directorio del script actual
    script_dir = os.path.dirname(__file__)
    # Construir la ruta completa al archivo JSON
    full_path = os.path.join(script_dir, fileName)
    try:
        with open(full_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"El archivo {fileName} no fue encontrado.")
        return None
    except json.JSONDecodeError:
        print(f"Error al decodificar JSON de {fileName}")
        return None

def saveJson(fileName, data):
    # Obtener la ruta del directorio del script actual
    script_dir = os.path.dirname(__file__)
    # Construir la ruta completa al archivo JSON
    full_path = os.path.join(script_dir, fileName)
    try:
        with open(full_path, 'w') as file:
            json.dump(data, file, indent=4)
    except FileNotFoundError:
        print(f"El archivo {fileName} no fue encontrado.")
    except json.JSONDecodeError:
        print(f"Error al decodificar JSON de {fileName}")

def createNewJson(data):
    storage_length = getJson("../data/ddbb/amount.json")["amount"]
    # Obtener la ruta del directorio del script actual
    script_dir = os.path.dirname(__file__)
    # Construir la ruta completa al archivo JSON
    full_path = os.path.join(script_dir, '../data/ddbb/', f"{storage_length+1}.json")

    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    # Escribir los datos en el archivo JSON
    with open(full_path, 'w') as file:
        json.dump(data, file, indent=4)

    saveJson("../data/ddbb/amount.json", {"amount": storage_length + 1})

def getLastUpdatedJson():
    defaultContent = backupJson0()
    storage_length = 0
    file = getJson("../data/ddbb/0.json")
    # Obtener la ruta del directorio del script actual
    script_dir = os.path.dirname(__file__)
    # Construir la ruta completa al archivo JSON

    if file == None:
        print("No hay archivos de almacenamiento")
        # Obtener la ruta del directorio del script actual
        script_dir = os.path.dirname(__file__)
        # Construir la ruta completa al archivo JSON
        full_path = os.path.join(script_dir, '../data/ddbb/', f"0.json")
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        # Escribir los datos en el archivo JSON
        with open(full_path, 'w') as file:
            json.dump(defaultContent, file, indent=4)
        return defaultContent
    else:
      while file != None:
          storage_length += 1
          file = getJson(f"../data/ddbb/{storage_length}.json")
      file = getJson(f"../data/ddbb/{storage_length-1}.json")
      return file


def createInforme(resultados):
    # Obtener la ruta completa del directorio
    script_dir = os.path.dirname(__file__)
    full_path = os.path.join(script_dir, '../data/ddbb/', 'resultados.json')
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
    # valido que exista la ruta para salvar en caso de excepcion 
    if os.path.exists(full_path):
        with open(full_path, 'r') as file:
            try:
                informes = json.load(file)
            except json.JSONDecodeError:
                print("El archivo JSON de resultados no existe. Se creara un nuevo archivo de resultados.json")
                informes = {}
    else:
        informes = {}

    storage_length = getJson("../data/ddbb/amount.json")["amount"]
    informes[storage_length] = resultados
        
    # Escribir el contenido actualizado de nuevo en el archivo
    with open(full_path, 'w') as file:
        json.dump(informes, file, indent=4)