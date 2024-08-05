from ninjas import *

misiones = ["Asesinar","Espiar","Capturar","Escoltar"]

def menumision():
    print("Seleccione la mision que desea asignarle al ninja --->")
    cont = 1
    for i in misiones:
        print(cont,i)
        cont += 1
    opc = int(input("Ingrese la opción deseada : "))
    return opc

def agregarnueva_mision():
    print("")
    misiones.append(input("Ingrese la nueva mision que desea agregar: "))
    print("")
    print("------------------------------------------------------")
    print("------------ MISION AGREGADA EXITOSAMENTE ------------")
    print("------------------------------------------------------")

