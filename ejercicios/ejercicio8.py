"""
Autor: Roberto Jaime Rico Sandoval.
Fille: Estructuras vcondicionales.
Date: 28/ 07/ 2022
Folio: 964NB09

"""

import random


# Ejercicio 1

print("Ingresa dos números a dividir\nNo se puede dividir por cero.")
num1 = float(input("Ingesa el primer número:  "))
num2 = float(input("Ingesa el segundo número:  "))

while num2 == 0: 
    print("\nNo se puede dividir el número cero. Vuelve a intentarlo.")
    num2 = float(input("Ingesa el segundo número:  "))

if (num1 % num2 == 0):
    print(f"la división entre {num1} y {num2} es exacta.\nResultado: ({round(num1 / num2)})")
else:
    print(f"la división entre {num1} y {num2} no es exacta.\nResultado: ({num1 / num2})")


# Ejercicio 2.

calificacion = random.uniform(0, 9)

if calificacion <= 6:
    print(f"El estudiante esta reprobado efe :'(\n{round(calificacion,1)}")

elif calificacion > 6 and calificacion <= 7:
    print(f"Calificación suficiente: {round(calificacion,1)}")

elif calificacion > 7 and calificacion <= 9:
    print(f"Buen desempeño: {round(calificacion,1)}")

elif calificacion > 9 and calificacion <= 10:
    print(f"Destacado: {round(calificacion,1)}")



# Ejercicio 3.

print("\nBienbenido al Spotififi. ¿Qué plan deseas contratar?\n1) Individual\n2) Estudiante\n3) Duo\n4) Familiar")

precio = 0
pregunta = int(input("\n\nDigita el número de tu plan a seleccionar: "))

while pregunta < 1 or pregunta > 4:
    print(f"Dato no existente [{pregunta}]. Vuelve a intentarlo.")
    pregunta = int(input("\n\nDigita el número de tu plan a seleccionar: "))

if pregunta == 1:
    precio = 115
    print(f"\nHas seleccionado un plan individual (1)\nSu precio es de: ${precio}")

elif pregunta == 2:
    precio = 60
    print(f"\nHas seleccionado un plan estudiantil (2)\nSu precio es de: ${precio}")

elif pregunta == 3:
    precio = 150
    print(f"\nHas seleccionado un plan duo (3)\nSu precio es de: ${precio}")

elif pregunta == 4:
    precio = 180
    print(f"\nHas seleccionado un plan familiar (4)\nSu precio es de: ${precio}")



 
# Ejercicio 4.

print("\nIntroduce un año, para comprobar si es un año biciesto.")
year = int(input("Año: "))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(f"\nEl año {year} es biciesto. No cumplen años los del 35 de febrero xD")
else:
    print(f"\nEl año {year} no es biciesto.")



# Ejercicio 5

print(f"Encontrar el factorial de un número")
numero = random.randrange(0, 11)
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



# Ejercicio 6

escuela = []
incremento = 0
p = 0

# Ingresar datos.
alumnos = int(input("¿Cunátos alumnos hay?\n\- "))

escuela.append(alumnos)

for c in range(alumnos):
    incremento += 1
    calificacion = float(input(f"Ingresa la calificación del alumno: {incremento}: "))
    escuela.append(calificacion)

    p += calificacion

# Total de alumnos.
print(f"\nHay un total de {escuela[0]} alumnos.")

# Promedio general del grupo.
promedio = (p/alumnos)
print(f"\nPromedio general del grupo {promedio}")

# Calificación mínima encontrada.
print(f"Calificación mínima {min(escuela[1:])}")

# Calificación máxima encontrada..
print(f"Calificación mínima {max(escuela[1:])}")



