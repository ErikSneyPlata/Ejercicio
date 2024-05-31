import empleados, registro

while True:
    print("************************************************************")
    print("                  sistema de empleados")
    print("************************************************************")
    opt=int(input("1.Registrar\n2.Mostrar empleados\n3.modificar empleados\n4.despedir empleado (Elimina)\n5.Registrar entrada de empleado\n6.Registrar salida de empleado\nIngrese su opcion: "))
    if opt==1:
        empleados.registro()
    elif opt==2:
        empleados.mostrar_empleados()
    elif opt==3:
        empleados.modificar_empleado()
    elif opt==4:
        empleados.despedir_empleado()
    elif opt==5:
        registro.entrada()
    elif opt==6:
        registro.salida()
    elif opt==7:
        break


