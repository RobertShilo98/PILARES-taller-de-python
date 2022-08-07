"""
Autor: Roberto Jaime Rico Sandoval
Fille: Ejercicio 5 de la práctica 4.
Date: 05/ 08/ 2022
Folio: 964NB09

"""

operador = True
mYear = ("Comienzo de lista default", "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

while operador == True:
    print("\nPara salir selecciona 0 o un número menor a 0")
    seleccion = int(input("Coloca el número del mes que quieres acceder  -  "))

    if seleccion <= 0:
        print("\nSaliendo del sistema")
        break

    elif seleccion > 12:
        print(f"\nDato erroneo {seleccion}")

    elif seleccion > 0 and seleccion < 12:
        print(f"\nRecorrido de la tupla: {mYear[seleccion:]}")

