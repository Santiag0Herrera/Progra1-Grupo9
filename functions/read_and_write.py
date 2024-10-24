import json
import os

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
    defaultContent = {"matias": "hola"}
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
          print(storage_length)
          storage_length += 1
          file = getJson(f"../data/ddbb/{storage_length}.json")
      file = getJson(f"../data/ddbb/{storage_length-1}.json")
      return file
