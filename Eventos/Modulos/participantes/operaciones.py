def registrar_participante(data):
    print("**************************************************")
    participante = {}
    doc = input("Ingrese el documento: ")    
    if data["participantes"].get(doc, None) == None:
        participante["Nombre"] = input("Ingrese el nombre: ")
        participante["Edad"] = int(input("Ingrese la edad: "))
        participante["Cargo"] = input("Ingrese el cargo: ")
        participante["Pago"] = False
        data["participantes"][doc] = participante
    else:
        print("Participante ya existe!")
    print("**************************************************")

def pagar_participante(data):
    print("**************************************************")
    doc = input("Ingrese el documento: ")
    participante = data["participantes"].get(doc, None)
    if participante != None and participante["Pago"] == False:
        data["participantes"][doc]["Pago"] = True
        print("Pago existoso!")
    else:
        print("Participante no existe o ya pagó!")
    print("**************************************************")

def eliminar_participante(data):
    print("**************************************************")
    doc = input("Ingrese el documento: ")
    participante = data["participantes"].get(doc, None)
    if participante != None and participante["Pago"] == False:
        data["participantes"].pop(doc)
        print("Eliminación existosa!")
    else:
        print("Participante no existe o ya perdió!")
    print("**************************************************")