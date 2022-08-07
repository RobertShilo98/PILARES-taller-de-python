"""
Autor: Roberto Jaime Rico Sandoval
Fille: Tipos de datos en Python.
Date: 20/ 07/ 2022
Folio: 964NB09

"""

celcius = -32 

c = int(input("Ingresa los grados fahrenheit: "))
print(f"Haz ingresado: {c} F")

convertor = (c - celcius) * 5/9

print(f"Conversion de grados fahrenheit a celcius: {round(convertor,1)} C")


############

num1 = float(input("\n\nPrimer número - "))
num2 = float(input("Segundo número - "))

suma = (num1 + num2)
resta = (num1 - num2)
multi = (num1 * num2)
div = (num1 / num2)

print(f"Suma: {suma}\nResta: {resta}\nMultiplicación: {multi}\nDivisión: {div}")


############

base = float(input("\n\nIngesa la base del rectángulo: "))
altura = float(input("\n\nIngesa la altura del rectángulo: "))

area = (base * altura)
print(f"La base del rectángulo es de: {area} m2")

############

num1 = float(input("\n\nPrimer número - "))
num2 = float(input("Segundo número - "))
num3 = float(input("Tercer número - "))

media = (num1 + num2 + num3 )/3
print(f"La media encontrada es de: {media}")

