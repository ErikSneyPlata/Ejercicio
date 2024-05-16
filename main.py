import json
import registro
        
def main():
    while True:
        opcion = ("Que accion desea realizar:\n1.registrar participante\n2.ranking participantes\n3.eliminar participantes\n4.salir")
        if opcion == 1:
            registro.registro_participantes()
        if opcion == 2:
            ranking.posicion_participantes()
        if opcion == 3:
            eliminar.eliminar_participantes()
        if opcion == 4:
            break #confirmacion para salir

