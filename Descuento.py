# Definir cantidad de descuento según el precio de la compra
def calcular_descuento(importe_compra):
    if 100 <= importe_compra <= 500:
        descuento = importe_compra * 0.05
    elif importe_compra > 500:
        descuento = importe_compra * 0.08
    elif importe_compra < 100:
        descuento = print ("Lo sentimos, no hay ningún descuento aplicable")
    return descuento

# Input del precio de la compra
importe_compra = float(input("Ingrese el importe de la compra: "))

# Resultado del calculo del descuento
descuento = calcular_descuento(importe_compra)
print("El importe del descuento es:", descuento, "€")