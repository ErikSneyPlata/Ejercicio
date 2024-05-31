def mostrar_eventos(data):
    print("**************************************************")
    print("Los eventos son:")
    for valor in data["eventos"]:
        print("-",valor["Nombre"], ", con locación",valor["Locacion"], ", el dia", valor["Dia"])    
    print("**************************************************")