import csv
import os


def buscar_informacion(ruta_archivo, nombre, modo='TODO'):
    ''' busca la informacion requerida por parametro, sobre el usuario ingresado y devuelve una lista'''
    lista = []
    with open(ruta_archivo, "r") as file:
        reader = csv.reader(file, delimiter=",")
        next(reader)

        for alum in reader:
            act_nom = alum[1]  # me guardo el nombre
            contexto = alum[3]
            if act_nom == nombre:
                if modo == 'TODO':
                    lista.append(alum)
                elif modo == 'EXPLICACION' and 'BigBlueButton: Sala de VC de explicaciones de práctica' in contexto:
                    lista.append(alum)
                elif modo == 'TEORIA' and 'Página: Material de las clases' in contexto:
                    lista.append(alum)
    return lista


def mostrar_actividad_usuario(actividades):
    """Muestra la actividad del usuario"""
    print(f"Usuario: {actividades[0][1]}")
    print("-" * 50)
    print("{:<20} {:<20} {:<15}".format(
        "Dia/hora", "Recurso accedido", "Dir IP"))
    print("-" * 50)
    for actividad in actividades:
        fecha = actividad[0]
        # mostrar solo los primeros 20 caracteres del recurso
        recurso = actividad[3][:20]
        ip = actividad[6]
        print("{:<20} {:<20} {:<15}".format(fecha, recurso, ip))


actividades = buscar_informacion('log_catedras.csv', 'Staryu')
mostrar_actividad_usuario(actividades)
