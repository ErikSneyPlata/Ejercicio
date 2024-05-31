import json

def lectura_json():
    try:
        with open('empresa_trabajadores//datos.json','r') as leer:
            datos=json.load(leer)
            return datos
    except FileNotFoundError:
        return {}
    
def guardar_json(data):
    with open("empresa_trabajadores//datos.json","w") as guardar:
        json.dump(data,guardar,indent=4)

def registro():
    data=lectura_json()
    
    nombre=input("Ingrese el nombre: ")
    edad=int(input("Ingrese la edad: "))
    numero_telefono=input("Ingrese el numero de telefono: ")
    direccion=input("Ingrese la direccion: ")
    documento=int(input("Ingrese el documento: "))
    if data.get(documento, None)==None:
        data[documento]={
            "nombre":nombre,
            "edad":edad,
            "numero telefono":numero_telefono,
            "direccion":direccion,
        }
        guardar_json(data)
        print("\nGUARDANDO...\n")
        print("\nSE HA GUARDADO EXITOSAMENTE...\n")
        
    else:
        print("El empleado ya exite")

    
def mostrar_empleados():
    datos=lectura_json()
    cont=1
    for doc in datos.values():
        print("\nEmpleado ",cont)
        for key, value in doc.items():
            print(key,": ",value)
        cont+=1

def despedir_empleado():
    data = lectura_json()
    doc=input("\ningrese el documento: ")
    if doc in data:
        del data[doc]
        print("\nEliminado correctamente...\n")
        guardar_json(data)
        return
    else: 
        print("No se encontro el documento")
        