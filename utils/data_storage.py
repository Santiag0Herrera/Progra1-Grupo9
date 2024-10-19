import json

def obtener_provincias():
    try:
        with open('/home/santiago/Desktop/PrograI/Progra1-Grupo9/utils/provincias.json', 'r') as file:
            provinces = json.load(file)
        return provinces
    except FileNotFoundError:
        print("The file 'provincias.json' was not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON from 'provincias.json'.")
        return None