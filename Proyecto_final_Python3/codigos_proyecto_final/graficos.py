"""
Autor: Roberto Jaime Rico Sandoval.
Folio: 964NB09
Date: 18/ 08/ 2022
Fille: Gráficos.
"""

from itertools import count
from palabras import *

def ahorcado():

    aciertos = {}
    barra = []
    
    cuerda = ""

    intentos = salida = 0
    contador = 1

    word = words()
    juego = len(word)

    for i in range(juego):
        cuerda += "_"
    
    print(cuerda)    
    for p in word:
        barra.append(p)
        
    print(barra)
    monito = [
        "  |",
        "  |",
        " ( )",
        "--|-- ",
        "  | ",
        " / \ "]


    print(f"\nEl estado a adivinar tiene {len(cuerda)} carácteres")

    while intentos < 6 and salida < len(cuerda):

        
        letra = str(input(f"\nIntroduce tu {contador} primera letra  -  "))

        if letra in word:
            print(f"\nCorrecto, la letra {letra} se encuentra en la palabra a adivinar.")

            contador += 1
            salida += word.count(letra)

            print(f"\nTotal de letras a adivinar: {len(cuerda)}")
            print(f"Total de letras adivinadas: {salida}")
            
            print(f"\nTotal de errores: {intentos}\nTe restan {6 - intentos} intentos")
            
            aciertos[letra] = word.count(letra)
            
            print("\n ** Incidencias ** ")
            for llaves, valores in aciertos.items():
                print(f"{llaves} tiene {valores} coincidencias en la palabra buscada.")

            conteo = word.count(letra)
            arranque = 0

            for i in range(conteo):     
                position = word.find(letra,arranque)
                cuerda = cuerda[:position] + letra + cuerda[position + 1 :]
                arranque = position + 1
    
            print(cuerda)
            
        else:
            print(f"\nLetra {letra} no encontrada.")
            print(cuerda)
            intentos += 1
            contador += 1

            for i in range(intentos):
                print(monito[i])
                
            print(f"\nTotal de errores: {intentos}\nTe restan {6 - intentos} intentos")
            
            print("\n ** Incidencias ** ")
            for llaves, valores in aciertos.items():
                print(f"{llaves} tiene {valores} coincidencias en la palabra buscada.")

    if salida == len(cuerda):
        print(f"\nFelicidades acabas de adivinar la palabra {word}")

    elif intentos >= 6:
        print(f"\nNo lograstes adivinar la palabra {word}")

    else:
        print(f"\nNo lograstes adivinar la palabra {word}")
    

