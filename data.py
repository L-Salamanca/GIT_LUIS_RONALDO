import json

def guardar_datos(data, filename='ninjas.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def cargar_datos(filename='ninjas.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}