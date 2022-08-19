"""
Autor: Roberto Jaime Rico Sandoval.
Fille: Ejercicio 2 filtrado por map.
Date: 18/ 08/ 2022
Folio: 964NB09
"""

tuplaNumerica = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)

def comprobador(n):
    if n > 5:
        return n

tuplaMapeada = tuple(map(comprobador, tuplaNumerica))
tuplaFiltrada = tuple(filter(comprobador, tuplaNumerica))

print(f"\nNúmeros: {tuplaNumerica}")
print(f"\nNúmeros mapeados: {tuplaMapeada}")
print(f"\nNúmeros filtrados: {tuplaFiltrada}")

