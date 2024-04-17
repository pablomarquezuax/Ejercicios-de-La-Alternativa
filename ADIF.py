def calcular_descuento(num_niños):
    if num_niños == 2:
        descuento = 0.10
    elif num_niños == 3:
        descuento = 0.15
    elif num_niños == 4:
        descuento = 0.18
    elif num_niños > 4:
        descuento = 0.18 + (num_niños - 4) * 0.01
    else:
        descuento = 0
    return descuento

# Solicitar al usuario que ingrese la cantidad de niños en la familia
num_niños = int(input("Ingrese la cantidad de niños en la familia: "))

# Calcular el descuento
descuento = calcular_descuento(num_niños)

# Mostrar el descuento aplicado
print("El descuento aplicado es del {:.2%}".format(descuento))
