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