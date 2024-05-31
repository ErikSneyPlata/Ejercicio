import json
import Ejecicio_carrera.participantes as participantes

datos={}        

def main():
    while True:
        print("Bienvenidos a sistema de registro deportivo Xtreme\n")
        print("************************************************************")
        print("                     MENU PRINCIPAL")
        print("************************************************************")

        opcion = ("Que accion desea realizar:\n1.menu participantes\n2.obtener resultados\n3.salir")
        if opcion == 1:

        if opcion == 2:
            ranking.posicion_participantes()
        if opcion == 3:
            break 

def submenu_participantes():
    print("************************************************************")
    print("                     MENU PARTICIPANTES")
    print("************************************************************")
    opt=int(input("1.Registrar participantes\n2.eliminar participantes"))
    if opt == 1:
        print("************************************************************")
        print("                       REGISTRO")
        print("************************************************************")
        participantes.registro_participantes()
    elif opt == 2:
        print("************************************************************")
        print("                    ELIMINAR PARTICIPANTE")
        print("************************************************************")
        eliminar.eliminar_participantes()