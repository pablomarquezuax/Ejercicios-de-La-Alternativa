def calcular_media(notas):
    return sum(notas) / len(notas)

def evaluar_alumno(media):
    if media > 15:
        return "Alumno con talento"
    elif 12 <= media <= 15:
        return "Con capacidad"
    else:
        return "Debe reorientarse"

# Obtener las notas del usuario
notas = []
for i in range(4):
    nota = float(input("Ingrese la nota {} (entre 0 y 20): ".format(i+1)))
    notas.append(nota)

# Calcular la media
media = calcular_media(notas)

# Evaluar al alumno
evaluacion = evaluar_alumno(media)

# Mostrar resultados
print("La media de las notas es:", media)
print("Evaluación del alumno:", evaluacion)
