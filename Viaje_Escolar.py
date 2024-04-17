def calcular_coste_trayecto(num_alumnos):
    if num_alumnos <= 25:
        coste_trayecto = 67.30
    else:
        coste_trayecto = 61.00
    return coste_trayecto

def calcular_coste_comida(num_alumnos, dias_viaje):
    coste_comida = 3.50 * num_alumnos * dias_viaje
    return coste_comida

def calcular_coste_alojamiento(num_alumnos, dias_viaje):
    if num_alumnos < 30:
        precio_por_dia = 4.75
    elif 31 <= num_alumnos <= 35:
        precio_por_dia = 4.00
    else:
        precio_por_dia = 3.50
    coste_alojamiento = precio_por_dia * num_alumnos * dias_viaje
    return coste_alojamiento

# Solicitar al usuario que ingrese la cantidad de alumnos y los días de viaje
num_alumnos = int(input("Ingrese la cantidad de alumnos: "))
dias_viaje = int(input("Ingrese la cantidad de días de viaje: "))

# Calcular el coste total del trayecto, comida y alojamiento por alumno
coste_trayecto_por_alumno = calcular_coste_trayecto(num_alumnos)
coste_comida_por_alumno = calcular_coste_comida(num_alumnos, dias_viaje)
coste_alojamiento_por_alumno = calcular_coste_alojamiento(num_alumnos, dias_viaje)

# Calcular el coste total por alumno
coste_total_por_alumno = (coste_trayecto_por_alumno + coste_comida_por_alumno + coste_alojamiento_por_alumno)

# Calcular el coste total del viaje
coste_total_viaje = coste_total_por_alumno * num_alumnos

# Mostrar el coste total del viaje
print("El coste total del viaje es de {:.2f} €".format(coste_total_viaje))
