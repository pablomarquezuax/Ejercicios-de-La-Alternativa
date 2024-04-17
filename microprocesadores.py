def calcular_descuento(cantidad_componentes, cliente):
    if 10000 <= cantidad_componentes <= 20000:
        descuento = 0.10
    elif 20001 <= cantidad_componentes <= 40000:
        descuento = 0.15
    elif cantidad_componentes > 40000:
        descuento = 0.20
    else:
        descuento = 0
    
    # Reducción del descuento para el cliente COMMAQ
    if cliente == "COMMAQ":
        descuento -= 0.02
    
    # Descuento mejorado para el cliente BEL
    if cliente == "BEL":
        descuento += 0.01
    
    return descuento

# Solicitar al usuario que ingrese la cantidad de componentes y el nombre del cliente
cantidad_componentes = int(input("Ingrese la cantidad de componentes pedidos: "))
cliente = input("Ingrese el nombre de su empresa (COMMAQ, BEL u otro): ")

# Calcular el descuento
descuento = calcular_descuento(cantidad_componentes, cliente)

# Mostrar el descuento aplicado
print("El descuento aplicado es del {:.2%}".format(descuento))
