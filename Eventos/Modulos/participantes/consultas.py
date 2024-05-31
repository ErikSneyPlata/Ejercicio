def saber_cuantos_empleados_no_han_pagado(data):
    print("**************************************************")
    cont = 0
    for valor in data["participantes"].values():
        if valor["Pago"] == False:
            cont += 1
    print("Existen", cont, "Participantes por pagar")
    print("La deuda total es:", cont*50000)
    print("**************************************************")

def saber_cuales_empleados_no_han_pagado(data):
    print("**************************************************")
    print("Los participantes que no han pagado son:")
    for valor in data["participantes"].values():
        if valor["Pago"] == False:
            print("-",valor["nombre"], "que tiene el cargo de",valor["Cargo"])    
    print("**************************************************")