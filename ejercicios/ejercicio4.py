"""
Autor: Roberto Jaime Rico Sandoval
Fille: Listas.
Date: 20/ 07/ 2022
Folio: 964NB09

"""

# Declaración de listas.
lista = [8, 3, 50, 'a']

ListaNombres = ["Roberto", "Carlos", "Zahira", "Carmen", "Julio"]
print(ListaNombres)
print(type(ListaNombres))

print(ListaNombres[0])
print(ListaNombres[1])
print(ListaNombres[2])
print(ListaNombres[4])

listaNumeros = [1, 2, 3]

num = ["lista", [4, 5, 6]]

# Mátriz.
print(num)
print(num[0])
print(num[1][1])
print(num[1][0])
print(num[1][2])

# Números negativos / Recorrido descendente.
print(ListaNombres[-1])
print(ListaNombres[-2])

# Alterar índices.
ListaNombres[0] = "Jaime"
print(ListaNombres[0])

