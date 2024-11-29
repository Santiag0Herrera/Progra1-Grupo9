import json, os
from functions.backup import backupJson0
script_dir = os.path.dirname(__file__)

######### JSON FILES MANIPULATION #########
def getJson(fileName):
    full_path = os.path.join(script_dir, fileName)
    try:
        with open(full_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None

def saveJson(fileName, data):
    script_dir = os.path.dirname(__file__)
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
    full_path = os.path.join(script_dir, '../data/ddbb/', f"{storage_length+1}.json")
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as file:
        json.dump(data, file, indent=4)
    saveJson("../data/ddbb/amount.json", {"amount": storage_length + 1})

def getLastUpdatedJson():
    defaultContent = backupJson0()
    storage_length = 0
    file = getJson("../data/ddbb/0.json")
    if file == None:
        full_path = os.path.join(script_dir, '../data/ddbb/', f"0.json")
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
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
    full_path = os.path.join(script_dir, '../data/ddbb/', 'resultados.json')
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
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
    with open(full_path, 'w') as file:
        json.dump(informes, file, indent=4)


######### CSV FILES MANIPULATION #########
def verify_if_exists_csv(file_name):
    full_path = os.path.join(script_dir, '../data/', file_name)
    return os.path.exists(full_path)

def read_new_csv(file_name):
    full_path = os.path.join(script_dir, '../data/', file_name)
    try:
        with open(full_path, 'r') as f:
            content = f.read()
            return content
    except FileNotFoundError:
        print(f"El archivo {file_name} no fue encontrado.")
        return None

def create_new_empty_csv(file_name):
    full_path = os.path.join(script_dir, '../data/', file_name)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
  
def write_csv(file_name, content):
    full_path = os.path.join(script_dir, '../data/', file_name)
    try:
        with open(full_path, 'w') as f:
            f.write(content)
    except FileNotFoundError:
        print(f"El archivo {file_name} no fue encontrado...")
        return None