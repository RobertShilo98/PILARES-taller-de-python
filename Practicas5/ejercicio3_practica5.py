"""
Autor: Roberto Jaime Rico Sandoval
Fille: Tercer ejercicio práctica 5.
Date: 05/ 08/ 2022
Folio: 964NB09

"""

import random

cumulo = interes = 0

print("*** Sistema de ventas ***")

for ventas in range(5):
    compra = random.uniform(0, 500)
    print(f"\nPrimer compra ${round(compra,2)}")
    cumulo += compra

print(f"\n\nTotal bruto a pagar: ${round(cumulo,2)}")

interes = random.uniform (0.0, 0.9)

if interes > 0.3:
    print(f"\nVenta cancelada, el interés es mayor al 30%.\nInterés a pagar {round(interes * 100,2)}%")
else:
    print(f"\nInterés de la compra {round(interes * 100,2)}%")
    print(f"\nVenta aceptada, el interés es menor al 30%.\nTotal neto a pagar con interés: ${round(cumulo + interes * 100,2)}")

