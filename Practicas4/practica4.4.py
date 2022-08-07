"""
Autor: Roberto Jaime Rico Sandoval
Fille: Tercer ejercicio de la práctica 4
Date: 04/ 08/ 2022
Folio: 964NB09

"""

import random

nombresAlumnos = []
calificacionesAlumnos = []
caliAlumno = []

registro = {}

contador = 1
iterador = 1

suma = 0
sumaGeneral = 0

recolector = 0

bon = False

totalAlumnos = int(input("\n¿Cuántos alumnos hay en clase?  -  "))


while totalAlumnos > 10:

    print("\nNo puede haber más de 40 alumnos en el aula.")
    totalAlumnos = int(input("\n¿Cuántos alumnos hay en clase?  -  "))


for clase in range(totalAlumnos):

    nombreAlumno = str(input(f"\n¿Cuál es el nombre del {contador} alumno?  -  "))


    while nombreAlumno in nombresAlumnos:
        print(f"\nEste nombre ya a sido registrado, no se puede dúplicar.")
        nombreAlumno = str(input(f"\n¿Cuál es el nombre del {contador} alumno?  -  "))

    nombresAlumnos.append(nombreAlumno)

    totalCalificaciones = random.randrange(3,7)
    print(f"\n{nombreAlumno} tiene {totalCalificaciones} calificaciones.")

    while totalCalificaciones > 5:

        print("\nSolo puede tener máximo 5 calificaciones el alumno y solo puede tener números enteros")
        totalCalificaciones = random.randrange(3,7)
        print(f"\n{nombreAlumno} tiene {totalCalificaciones} calificaciones.")

    recolector += totalCalificaciones


    for cali in range(totalCalificaciones):

        calificacion = float(input(f"\nIngresa la calificación {iterador} del alumno {nombreAlumno}: "))

        while calificacion < 0 or calificacion > 10:

            print(f"\nError, la calificación solo puede ser mayor a 0 y menor a 10. Calificación registrada [{calificacion}]")
            calificacion = float(input(f"\nIngresa la calificación {iterador} del alumno {nombreAlumno}: "))

        calificacionesAlumnos.append(calificacion)
        caliAlumno.append(calificacion)

        suma += calificacion
        sumaGeneral += calificacion
        iterador += 1

    registro[nombreAlumno] = caliAlumno

    promedio = (round(suma/totalCalificaciones,1))
    print(f"\n\nPromedio del alumno {nombreAlumno}: {promedio}\n")

    if promedio >= 6:
        print(f"\n\n{nombreAlumno} aprobado.")
    else:
        print(f"\n{nombreAlumno} reprobado.")

    iterador = 1
    contador += 1
    caliAlumno = []
    suma = 0
    
print(f"\n\nTotal de registros: {registro}")
print(f"\n\nTotal de calificaciones: {calificacionesAlumnos}")
print(f"\n\nPromedio general de la clase: {round(sumaGeneral/recolector,1)}")

print("\n\nEscribe *exit* para terminar.")

while bon == False:

    consulta = str(input("\nColoca aquí el nombre del alumno al que quieras consultar sus calificaciones  -  "))

    if consulta == "exit":
        print("\n\nHasta pronto :)")
        bon = True

    elif consulta in registro:
        print(f"\n\nAlumno encontrado.\n{registro[consulta]}")
        bon = True

    else:
        print("\nAlumno no encontrado.")
        bon = False

