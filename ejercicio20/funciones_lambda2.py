"""
Autor: Roberto Jaime Rico Sandoval.
Fille: Función lambda ejercicio 2.
Date: 18/ 08/ 2022
Folio: 964NB09
"""

from functools import reduce
import random

lista1 = []
lista2 = []

doble = lambda x:x * 2
negativo = lambda y:y > 0

for i in range(1, 11):
    
    numero = random.randrange(2, 250)
    lista1.append(numero)
    
    numero2 = random.randrange(-101, 101)
    lista2.append(numero2)

print(f"\nLista ordinaria de números: {lista1}")

lista1Modi = list(map(doble, lista1))
print(f"\nEl doble de los números: {lista1Modi}")

lista2Modi = list(filter(negativo, lista2))
print(f"\nSolo números positivos: {lista2Modi}")

x = reduce(lambda x,y : x+y, lista1)
print(f"\nNúmero afectado por la función reduce: {x}")

