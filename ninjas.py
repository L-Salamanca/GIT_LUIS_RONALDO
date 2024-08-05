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
       