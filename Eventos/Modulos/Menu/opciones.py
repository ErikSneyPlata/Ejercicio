from eventos.consultas import *
from eventos.operaciones import *
from participantes.operaciones import *
from participantes.consultas import *
from Menu.opciones import *
from datos.datosEventos import *

opc_menu = ("1. Para registrar participante", "2. Para pagar", "3. Para eliminar participante", 
            "4. Para registrar un evento", "5. Para modificar un evento", "6. Para eliminar un evento", 
            "7. Para marcar un evento como completado", 
            "8. Para saber cuantos empleados no han cancelado aún el aporte", 
            "9. Para saber cuales empleados (listarlos) no han cancelado.", "10. Para mostrar eventos", 
            "11. Para salir")

def menu():
    print("Seleccione ->")
    for i in opc_menu:
        print(i)
    opc = int(input("Ingrese la opción deseada: "))
    return opc

def menu_principal():
    while True:
        print("*********************************************************")
        opc = menu()
        if opc == len(opc_menu):
            print("Saliendo...")
            break    
        elif opc == 1:
            registrar_participante(eventos)
        elif opc == 2:
            pagar_participante(eventos)    
        elif opc == 3:
            eliminar_participante(eventos)
        elif opc == 4:
            registrar_evento(eventos)
        elif opc == 5:
            print("Modificar evento")#Pendiente
        elif opc == 6:
            eliminar_evento(eventos)
        elif opc == 7:
            completar_evento(eventos)
        elif opc == 8:
            saber_cuantos_empleados_no_han_pagado(eventos)
        elif opc == 9:
            saber_cuales_empleados_no_han_pagado(eventos)
        elif opc == 10:
            mostrar_eventos(eventos)
        elif opc == 0:
            print(eventos["participantes"])
    

