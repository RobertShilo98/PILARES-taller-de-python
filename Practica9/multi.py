"""
Autor: Roberto Jaime Rico Sandoval.
Fille: Ejercicio 1 modulos.
Date: 18/ 08/ 2022
Folio: 964NB09
"""

import random

def calculo():
    
    positivo = negativo = 0
    
    aciertos = []
    errores = []
    
    for i in range(10):
        
        num1 = random.randrange(1, 11)
        num2 = random.randrange(1, 11)
        
        print(f"\nCálcula la multiplicación de {num1} x {num2}")
        
        accion = int(input("Respuesta:  -  "))
        
        if accion == num1 * num2:
    
            positivo += 1
            aciertos.append(positivo)
            
            print(f"\nCorrecto: {accion}")
        
        else:
            negativo += 1
            errores.append(negativo)
            
            print(f"\nIncorrecto: {accion}")
    
    if positivo > 1:
        print(f"\nTotal de aciertos: {aciertos[-1]}")
        
    else:
        print("\nNo hay acierto: 0")
    
    if negativo > 1:
        print(f"\nTotal de errores: {errores[-1]}")
    
    else:
        
        print("\nNo hay errores: 0")

calculo()
