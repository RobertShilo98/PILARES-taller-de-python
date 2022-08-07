"""
Autor: Roberto Jaime Rico Sandoval
Fille: Primer ejercicio de la práctica 4
Date: 04/ 08/ 2022
Folio: 964NB09

"""

import random

listaNumeros = []
listaNumerosCuadrados = []
listaNumerosCubicos = []

for e in range(10):
    numero = random.randrange(1, 10)
    listaNumeros.append(numero)

    cuadrado = (numero ** 2)
    listaNumerosCuadrados.append(cuadrado)

    cubico = (numero ** 3)
    listaNumerosCubicos.append(cubico)

print(f"\nNúmeros seleccionados: {listaNumeros}")
print(f"\nNúmeros seleccionados al cuadrado: {listaNumerosCuadrados}")
print(f"\nNúmeros seleccionados al cubo: {listaNumerosCubicos}")

