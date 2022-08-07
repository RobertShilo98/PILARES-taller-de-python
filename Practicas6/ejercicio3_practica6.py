"""
Autor: Roberto Jaime Rico Sandoval
Fille: Segundo ejercicio práctica 6.
Date: 06/ 08/ 2022
Folio: 964NB09

"""

numero = int(input("\n¿Hasta qué número contaré?  -  "))
i = 2

print(f"\nNumeros primos del 1 al {numero}")

if numero == 0 or numero == 1:
    print(f"\nEsto es una neutralidad: {numero}")
else:

    for comienzo in range(1):
        print(f"Número primo: {i}")
        i += 1
        print(f"Número primo: {i}")
        i += 2
        print(f"Número primo: {i}")
        i += 2
        print(f"Número primo: {i}")
        i += 4
        print(f"Número primo: {i}")

    for numy in range(i, numero):

        if numy % 2 == 0 or numy % 3 == 0 or numy % 5 == 0 or numy % 11 == 0 or numy % 7 == 0:
            pass
        else:
            print(f"Número primo: {numy}")

