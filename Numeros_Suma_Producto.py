def clasificar_numeros():
    # Solicitar al usuario que ingrese los números
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))

    # Calcular la suma y el producto
    suma = a + b
    producto = a * b

    # Ordenar los números de menor a mayor
    numeros_ordenados = sorted([producto, a, suma, b])
    return numeros_ordenados

# Llamar a la función y mostrar el resultado
resultado = clasificar_numeros()
print("Los números ordenados de menor a mayor respecto a su suma y producto son:", resultado)
