def calcular_prima_anual(accidentes, responsabilidad, kilometros, antiguedad):
    # Calcular la prima por accidentes
    if accidentes == 0:
        prima_accidentes = 1.0  # Prima completa
    elif accidentes == 1:
        prima_accidentes = 0.5  # Mitad de la prima
    elif accidentes == 2:
        prima_accidentes = 1/3  # Un tercio de la prima
    elif accidentes == 3:
        prima_accidentes = 1/4  # Un cuarto de la prima
    else:
        prima_accidentes = 0.0  # Prima anulada

    # Calcular la prima de distancia
    prima_distancia = min(400, 0.01 * kilometros)

    # Calcular la prima de antigüedad
    if antiguedad >= 4:
        prima_antiguedad = 200 + 20 * (antiguedad - 4)
    else:
        prima_antiguedad = 0

    # Calcular la prima total
    prima_total = prima_distancia + prima_antiguedad

    # Aplicar el ajuste por responsabilidad
    if responsabilidad > 20:
        prima_total *= prima_accidentes

    return prima_total

# Solicitar al usuario que ingrese los datos
accidentes = int(input("Ingrese el número de accidentes del conductor: "))
responsabilidad = float(input("Ingrese el porcentaje de responsabilidad del conductor: "))
kilometros = float(input("Ingrese la cantidad de kilómetros recorridos durante el año: "))
antiguedad = int(input("Ingrese los años de antigüedad del conductor: "))

# Calcular la prima anual del conductor
prima_anual = calcular_prima_anual(accidentes, responsabilidad, kilometros, antiguedad)

# Mostrar el resultado
print("La prima anual del conductor es de {:.2f} €".format(prima_anual))
