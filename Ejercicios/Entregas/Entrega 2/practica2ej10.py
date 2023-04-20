nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR', 'David',
'Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo', 'Francsica', 
'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan', 'Joaquina', 'Jorge',
'JOSE', 'Javier', 'Joaquín'  , 'Julian', 'Julieta', 'Luciana','LAUTARO', 'Leonel', 'Luisa', 
'Luis', 'Marcos', 'María', 'MATEO', 'Matias', 'Nicolás',  'Nancy', 'Noelia', 'Pablo', 
'Priscila', 'Sabrina', 'Tomás', 'Ulises', 'Yanina' '''

notas_1 = [81,  60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69, 12, 77,
           13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44, 85, 73, 37, 42, 95, 18, 7,
           74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37, 64, 13, 8,
           87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73, 95, 19, 47, 15, 31,
           39, 15, 74, 33, 57, 10]
"""
Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un programa que
manipule dichas estructuras de datos para poder resolver los siguientes puntos:

A Generar una estructura con todas las notas relacionando el nombre del estudiante con las notas. Utilizar 
  esta estructura para la resolución de los siguientes items.

B Calcular el promedio de notas de cada estudiante.

C Calcular el promedio general del curso.

D Identificar al estudiante con la nota promedio más alta.

E Identificar al estudiante con la nota más baja.

Nota:

 Las 3 estructuras están ordenadas de forma que los elementos en la misma posición corresponden a un mismo 
 alumno.
Realizar funciones con cada item
"""


def process_student_notes(nombres, notas_1, notas_2):
    ''' toma un string separados por comas y dos listas 
    de enteros y te devueve un diccionario con string como clave y una lista con dos enteros '''
    slogan = {clave: [n1, n2] for clave, n1, n2 in zip(nombres.replace(
        "'", "").replace("\n", "").replace(" ", "").split(","), notas_1, notas_2)}
    return slogan


slogan_a = process_student_notes(nombres, notas_1, notas_2)
#print(slogan_a)
# promedio notas cada estudiante


def average_eachother_student(slogan__a):
    ''' toma un dicionario que contiene una lista con dos enteros y devuelve un diccionario
    con el promedio de cada alumno '''
    average = {clave: sum(slogan__a[clave])/len(slogan__a[clave])
               for clave in slogan_a.keys()}
    return average


print(average_eachother_student(slogan_a))
# promedio general del curso


def all_average(slogan__a):
    ''' toma un diccionario que contiene una lista con dos enteros y devuelve el promedio general '''
    notas_totales = sum([sum(notes) for notes in slogan__a.values()])
    total_elementos = len(slogan__a)
    return notas_totales / total_elementos

print(all_average(slogan_a))
# Identificar al alumno que obtuvo la nota más alta


def up_average(slogan__a):
    ''' toma un string separados por comas y dos listas 
    de enteros y te devueve el alumno con la nota promedio mas alta '''
    averages = [(student,sum(notas)/len(notas)) for student,notas in slogan__a.items()]
    sorted_averages = sorted(averages,key=lambda x: x[1])
    return sorted_averages[-1][0]

print(up_average(slogan_a))
# Identificar al alumno que obtuvo la nota más baja


def lower_note(slogan__a):
    ''' toma un string separados por comas y dos listas 
    de enteros y te devueve el alumno con la nota mas baja '''
    students_min = [(name_student,min(valores)) for name_student, valores in slogan__a.items()]
    students_sorted = sorted(students_min,key=lambda x: x[1])
    return students_sorted[0][0]

print(lower_note(slogan_a))
