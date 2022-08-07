"""
Autor: Roberto Jaime Rico Sandoval.
Fille: colecciones de datos.
Date: 26/ 07/ 2022
Folio: 964NB09

"""

# Ejercicio 1.

listaNumeros = []
persona = []

num = 0

for elementos in range(1, 16):
    num += 1
    listaNumeros.append(num)

print(f"Múltiplos del 3 {listaNumeros[2:16:3]}")

# Ejercicio 2.

nombre = str(input("\n¿Cuál es tu nombre? -  "))
edad = int(input("\n¿Cuál es tu edad? -  "))
genero = str(input("\n¿Cuál es tu genero setzual 7u7? -  "))
estatura = float(input("\n¿Cuál es tu estatura? -  "))

persona.append(nombre)
persona.append(edad)
persona.append(genero)
persona.append(estatura)

print(f"\nDatos de la persona {persona}")

# Ejercicio 3.

profesiones = {

    "Claudia":"Repostera",
    "Juan":"Mecánico",
    "Ramiro":"Gigólo",
    "Pedro":"Narco",
    "Felipe":"Policia"
}

pregunta = str(input("¿De quíen quieres saber su profesión? -   "))
print(f"{profesiones[pregunta]}")

