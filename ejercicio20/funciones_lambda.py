"""
Autor: Roberto Jaime Rico Sandoval.
Fille: Función lambda.
Date: 18/ 08/ 2022
Folio: 964NB09
"""

import random

listaNumeros = []

funqui = lambda n:n % 2 == 0

for i in range(1, 11):
    
    num = random.randrange(10, 250)
    listaNumeros.append(num)
    
listaPar = list(filter(funqui, listaNumeros))

print(f"\nNúmeros pares: {listaPar}")

