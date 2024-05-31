import datos


def registrar_mascota():
    mascota = {}
    mascota["Tipo"] = input("Escriba el tipo de mascota (Ej: Perro): ")
    try:
        mascota["Nacimiento"] = int(input("Escriba la edad en dias de la mascota: "))
    except Exception:
        print("Ingrese un valor válido!")
        return
    mascota["Raza"] = input("Escriba la raza de la mascota (Ej: Criollo): ")
    datos.data.append(mascota)
    datos.guardar_datos()

def mostrar_mascotas():
    print("Las mascotas registradas son:")
    for mascota in datos.data:
        print("- Tipo:", mascota["Tipo"], "/ Nacimiento:", mascota["Nacimiento"], "/ Raza:", mascota["Raza"])
        