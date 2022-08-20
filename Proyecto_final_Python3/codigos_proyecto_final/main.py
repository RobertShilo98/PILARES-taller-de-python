"""
Autor: Roberto Jaime Rico Sandoval.
Folio: 964NB09
Date: 18/ 08/ 2022
Fille: Controlador / Menú.
"""

from graficos import *

comprobador = 0

while comprobador == 0:

    print("\n¿Quieres jugar al ahorcado?\n1- Sí\n2- No")
    eleccion = int(input("  -  "))

    while eleccion > 2 or eleccion < 1:

        print(f"\nDígito erroneo {eleccion}")
        print("\n¿Quieres jugar al ahorcado?\n1- Sí\n2- No")
        eleccion = int(input("\nElige  -  "))

    if eleccion == 1:
        print(f"\nAdivina un nombre de uno de los estados de la república mexicana. Tienes 6 intentos.")
        print("\nTodas las palabras comienzan con máyusculas y no hay espacios entre las palabras.")
        ahorcado()

    else:
        comprobador += 1
        print("\nSaliendo del juego. Hasta pronto :)")

