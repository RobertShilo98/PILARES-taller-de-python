"""
Autor: Roberto Jaime Rico Sandoval.
Fille: Ejercicio 2 Fnción MAP y FILTER.
Date: 18/ 08/ 2022
Folio: 964NB09
"""

listaNum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def numCuadrado(num):
    
    if num > 0:
        return num ** 2

listaModificada = list(map(numCuadrado, listaNum))

print(f"\nNúmeros al cuadrado: {listaModificada}")

