from enum import Enum

# Definición del tipo enumerado para los días de la semana
class DIA(Enum):
    DOMINGO = 0
    LUNES = 1
    MARTES = 2
    MIÉRCOLES = 3
    JUEVES = 4
    VIERNES = 5
    SÁBADO = 6

# Función para encontrar el día siguiente
def sucesor(dia):
    dia = (dia.value + 1) % 7  # Obtiene el valor numérico del día y calcula el siguiente
    return DIA(dia)  # Retorna el día siguiente como un objeto del tipo DIA

# Solicitar al usuario que ingrese un día de la semana
entrada_usuario = input("Ingrese un día de la semana (DOMINGO, LUNES, MARTES, MIÉRCOLES, JUEVES, VIERNES, SÁBADO): ")

# Convertir la entrada del usuario a un objeto del tipo DIA
dia_actual = DIA[entrada_usuario.upper()]

# Calcular el día siguiente
dia_siguiente = sucesor(dia_actual)

# Mostrar el resultado
print("El día siguiente a", dia_actual.name, "es", dia_siguiente.name)
