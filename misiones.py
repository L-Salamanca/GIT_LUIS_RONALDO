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

def asignarmision():
    print("-----------------------------------------------")
    while True:
        print("--------------------------------------------------------")
        opc = menumision()
        if opc == len(misiones)+1:
            print("Saliendo...")
            break    
        elif opc == 1:
            mis = misiones[0]
            break
        elif opc == 2:
            mis = misiones[1]
            break
        elif opc == 3:
            mis = misiones[2]
            break
        elif opc == 4:
            mis = misiones[3]
            break
        elif opc == 5:
            mis = misiones[4]
            break
        elif opc == 6:
            mis = misiones[5]
            break
        elif opc == 7:
            mis = misiones[6]
            break
        elif opc == 8:
            mis = misiones[7]
            break
    print("------------------------------------------------------")
    print("------------ MISION ASIGNADA EXITOSAMENTE ------------")
    print("------------------------------------------------------")
    return mis

def mostrarmisiones():
    print("LAS MISIONES DISPONIBLES SON : ")
    print("")
    for valor in misiones:
        print(valor)