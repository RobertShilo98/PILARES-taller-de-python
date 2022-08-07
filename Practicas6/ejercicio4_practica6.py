"""
Autor: Roberto Jaime Rico Sandoval
Fille: Cuarto ejercicio práctica 6.
Date: 06/ 08/ 2022
Folio: 964NB09

"""

import random

def factorial():
    print(f"Encontrar el factorial de un número")
    numero = random.randrange(0, 100)
    print(f"\nFactorial de: {numero}")

    g = 1
    i = 1

    if numero == 0:
        numero = 1
        print("El número es 0, por lo tanto, el factorial será 1.")

    for numeros in range(numero):

        g = (g*i)
        i += 1
        print(g)

factorial()

