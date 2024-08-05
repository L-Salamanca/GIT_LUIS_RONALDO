def ingresar_ninja(data):
    print("--------------------------------------------------")
    ninja = {}
    Nombre = input("Ingrese el Nombre del ninja que desea ingresar: ")    
    if data.get(Nombre, None) is None:
        ninja["Numero Misiones"] = int(input("Ingrese el numero de misiones que ha realizado el ninja a ingresar: "))
        ninja["Aldea"] = input("Ingrese la aldea a la que pertenece el ninja a ingresar: ")
        ninja["Rango"] = input("Ingrese el rango del ninja a ingresar: ")
        data[Nombre] = ninja
        guardar_datos(data)
        print("")
        print("-------------------------------------------")
        print("------ NINJA REGISTRADO EXITOSAMENTE ------")
        print("-------------------------------------------")
    else:
        print("LO SENTIMOS ESTE NINJA YA ESTA REGISTRADO EN NARUTOMANIA")
    print("")
    print("")
    
def modificar_ninja(data):
    print("--------------------------------------------------")
    ninja = {}
    Nombre = input("Ingrese el Nombre del ninja que desea modificar: ")    
    if data.get(Nombre, None) is not None:
        ninja["Numero Misiones"] = int(input("Ingrese el numero de misiones que ha realizado el ninja a modificar: "))
        ninja["Aldea"] = input("Ingrese la aldea a la que pertenece el ninja a modificar: ")
        ninja["Rango"] = input("Ingrese el rango del ninja a modificar: ")
        data[Nombre] = ninja
        guardar_datos(data)
        print("")
        print("-------------------------------------------")
        print("------ NINJA MODIFICADO EXITOSAMENTE ------")
        print("-------------------------------------------")
    else:
        print("LO SENTIMOS, ESTE NINJA NO ESTA REGISTRADO EN NARUTOMANIA")
    print("")
    print("")
    
def mostrarninjas(data):
    print("--------------------------------------------------")
    for nombre, info in data.items():
        print(f"Nombre: {nombre}")
        for key, value in info.items():
            print(f"{key}: {value}")
        print("--------------------------------------------------")
    print("")
    print("")
       