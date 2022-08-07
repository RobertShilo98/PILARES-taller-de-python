"""
Autor: Roberto Jaime Rico Sandoval
Fille: Tercer ejercicio práctica 6.
Date: 06/ 08/ 2022
Folio: 964NB09

"""

meses = 20

a = b = inicio = 10
mes = 1
x = 0

print(f"\npago del {mes} mes: {inicio} €\n")

for factor in range(meses-1):
    a = (a+b)
    b += 10
    mes += 1
    print(f"pago en factorial del mes {mes}: {a} €")

mes = 1
print(f"\n\npago del {mes} mes: {inicio} €\n")
mes += 1

for factor in range(meses-1):
    x += 2
    print(f"pago en múltiplo del mes {mes}: {inicio * x} €")
    mes += 1

