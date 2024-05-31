import gestionmascotas
import datos

def menu_principal():
    datos.cargar_datos()
    while True:
        print("**********************************")
        print("Ingrese:\n1. Para registrar mascotas\n2. Para mostrar mascotas registradas\n3. Para salir")
        opc = 0
        try:
            opc = int(input("Ingrese la opción deseada: "))
        except Exception:
            print("Valor incorrecto!!")            
        if opc == 1:
            gestionmascotas.registrar_mascota()
        elif opc == 2:
            gestionmascotas.mostrar_mascotas()
        elif opc == 3:
            print("Saliendo...")
            break
        else:
            print("La opción no es válida!")