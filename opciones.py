from ninjas import *
from misiones import *

opc_menup = ("1. Ingresar Ninja","2. Modificar Ninja","3. Eliminar Ninja","4. Mostrar Ninjas","5. Agregar Misiones","6. Asignar Misiones","7. Para salir")

def menup():
    print("      ::::    :::     :::     :::::::::  :::    ::: ::::::::::: ::::::::    :::   :::       :::     ::::    ::: :::::::::::     ::: ") 
    print("     :+:+:   :+:   :+: :+:   :+:    :+: :+:    :+:     :+:    :+:    :+:  :+:+: :+:+:    :+: :+:   :+:+:   :+:     :+:       :+: :+: ")
    print("    :+:+:+  +:+  +:+   +:+  +:+    +:+ +:+    +:+     +:+    +:+    +:+ +:+ +:+:+ +:+  +:+   +:+  :+:+:+  +:+     +:+      +:+   +:+ ")
    print("   +#+ +:+ +#+ +#++:++#++: +#++:++#:  +#+    +:+     +#+    +#+    +:+ +#+  +:+  +#+ +#++:++#++: +#+ +:+ +#+     +#+     +#++:++#++: ")
    print("  +#+  +#+#+# +#+     +#+ +#+    +#+ +#+    +#+     +#+    +#+    +#+ +#+       +#+ +#+     +#+ +#+  +#+#+#     +#+     +#+     +#+ ")
    print(" #+#   #+#+# #+#     #+# #+#    #+# #+#    #+#     #+#    #+#    #+# #+#       #+# #+#     #+# #+#   #+#+#     #+#     #+#     #+#  ") 
    print("###    #### ###     ### ###    ###  ########      ###     ########  ###       ### ###     ### ###    #### ########### ###     ### ")
    print("")
    print("")
    for i in opc_menup:
        print(i)
    opc = int(input("Ingrese la opción deseada: "))
    return opc

def menu_principal():
    while True:
        print("")
        print("")
        opc = menup()
        if opc == len(opc_menup):
            print("Saliendo...")
            break
        elif opc == 1:
            ingresar_ninja(ninjas)
        elif opc == 2:
            modificar_ninja(ninjas)
        elif opc == 3:
            eliminar_ninja(ninjas)
        elif opc == 4:
            mostrarninjas(ninjas)
        elif opc == 5:
            agregarnueva_mision()
        elif opc == 6:
            asignarmision(ninjas)
                     