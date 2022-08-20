"""
Autor: Roberto Jaime Rico Sandoval.
Folio: 964NB09
Date: 19/ 08/ 2022
Fille: Excepciones.
"""

from decimal import DivisionByZero


def divison():
    
    # Evaluador hasta que try sea verdadero.
    while True:
        
        # Intantar resolver está operación.
        try:
            a = float(input("Número 1: "))
            b = float(input("Número 2: "))
            
            print(a / b)
            
            break
        
        # Manejo de excepciones por medio de los nombre del error.
        except ZeroDivisionError:
            print(f"\nNo se puede dividir entre cero.")
            
        except ValueError:
            print(f"\nNo se puede dividir letras.")
        
        # Declaración opcional al terminal un bloque try.
        finally:
            print("Fin de la función")
        
divison()

