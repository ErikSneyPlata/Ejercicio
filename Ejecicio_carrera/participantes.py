import json


def leer_crear_json():
    try:
        with open("datos.json", "r") as lectura:
            datos = json.load(lectura)
            return datos
    except FileNotFoundError:
        return []
    

def guardar_json(datos):
    with open("datos.json", "w") as guardar:
        json.dump(datos, guardar, indent=4)
    print("\nGUARDANDO...\n")
        
def registro_participante():
    datos=leer_crear_json()
    nombre=input("ingrese el nombre: ")
    while True:
        try:
            edad = int(input("ingrese su edad: "))
            if edad<18:
                print("LO SIENTO, NO PUEDE PARTICIPAR")
                break
            else:
                break
        except ValueError:
            print("ingresa un numero para validar tu edad")
    if edad<18:return
    while True:
        try:       
            genero_validacion = int(input("1. Masculino\n2. Femenino\n3. No definido\n\nElija una opcion: "))
            if genero_validacion ==1: 
                genero="Masculino"
                break
            elif genero_validacion ==2: 
                genero="Femenino"
                break
            elif genero_validacion ==3: 
                genero="No definido"
                break
            else: 
                print("Ingresa una opcion valida dentro de las mostradas\n")
        except ValueError as e:
            print("Ingresa un numero, no una palabra")    
            print(f"Error: {e}")
            
    validacion_sandereano=input("ingrese el departamento de donde es oriundo: ")
    validacion_sandereano=validacion_sandereano.lower()
    if validacion_sandereano != "santander":
            return print("LO SIENTO, NO PUEDE PARTICIPAR")

    print("\n\nCARRERA EN LA QUE QUIERE PARTICIPAR: ")
    carrera = int(input("\n1. Atletismo \n2. Ciclismo\n3. Patinaje\n\nElija una opcion: "))
    while True:
        try:
            if carrera ==1: 
                carrera_seleccionada="Masculino"
                break
            elif carrera ==2: 
                carrera_seleccionada="Femenino"
                break
            elif carrera ==3: 
                carrera_seleccionada="No definido"
                break
            else: print("No ingresaste una opcion valida")
        except ValueError:
            print("ingresa un numero para validar la carrera en la que quieres estar")

    
    participante = {
        "nombre":nombre,
        "edad":edad,
        "genero":genero,
        "departamento":validacion_sandereano,
        "carrera seleccionada":carrera_seleccionada
    }
    datos.append(participante)
    guardar_json(datos)
    print("\n\n\nGUARDADO...")
        
registro_participante()
