import json

def lectura_json():
    try:
        with open('datos.json','r') as leer:
            datos=json.load(leer)
            return datos
    except FileExistsError:
        return {}
    
def guardar_json(data):
    with open("datos.json","w") as guardar:
        json.dump(data,guardar)

def registro():
    datos=lectura_json()

    nombre=input("Ingrese el nombre: ")
    edad=int(input("Ingrese la edad: "))
    numero_telefono=input("Ingrese el numero de telefono: ")
    direccion=input("Ingrese la direccion: ")
    documento=int(input("Ingrese el documento: "))

    datos[documento]={
        "nombre":nombre,
        "edad":edad,
        "numero telefono":numero_telefono,
        "direccion":direccion,
    }
    guardar_json(datos)

    
def mostrar_empleados():
    datos=lectura_json()
    cont=1
    for doc in datos:
        print("Empleado "+cont)
        for key, value in doc:
            print(key+": "+value)
        cont+=1
