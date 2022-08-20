"""
Autor: Roberto Jaime Rico Sandoval.
Folio: 964NB09
Date: 19/ 08/ 2022
Fille: Excepciones 2 / Raices cuadradas.
"""
import math


def cuadrado():
    
    """
    while True:
        try:
            cu = float(input("\nIngresa un número, para calcular su cuadrado:  -  "))
            print(math.sqrt(cu))
            break
        
        except ValueError:
            print("\nNo se permite ingresar letras, signos, y números negativos, solo números positivos.")
    """
        
    cu = float(input("\nDame un valor."))
        
    if cu < 0:
        raise ValueError ("\nNo se permiten números negativos")
    else:
        print(f"\nRáiz del número {cu} = {cu ** 1.5}") 
        
cuadrado()

