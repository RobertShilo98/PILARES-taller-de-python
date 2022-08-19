"""
Autor: Roberto Jaime Rico Sandoval.
Fille: Ejercicio 1 modulos.
Date: 18/ 08/ 2022
Folio: 964NB09
"""

print("\nResuelve las siguientes multiplicaciones.")

from multi import *

port = 0

while port == 0:

    print("\n¿Quieres seguir prácticando?\n1) sí\n2) No")

    accion = int(input("  -  "))

    while accion > 2 or accion < 1:

        print(f"Dato erroneo {accion}. Vuelve a intentarlo.")
        accion = int(input("  -  "))

    if accion == 1:
        
        calculo()
    else:

        port += 1
        print("Hasta pronto :)")

