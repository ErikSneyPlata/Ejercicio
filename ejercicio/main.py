import empleados

print("sistema de empleados")
opt=int(input("1.Registrar\n2.Mostrar empleados\n3.modificar empleados\n4.despedir empleado (Elimina)\n5.Registrar entrada de empleado\n6.Registrar salida de empleado\nIngrese su opcion: "))
if opt==1:
    empleados.registro()
elif opt==2:
    empleados.mostrar_empleados()


