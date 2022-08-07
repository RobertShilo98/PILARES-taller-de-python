"""
Autor: Roberto Jaime Rico Sandoval
Fille: Tipos de datos en Python.
Date: 20/ 07/ 2022
Folio: 964NB09

"""

"""
*** TIPOS DE DATOS ***

int = Números enteros.
float = Números decimales.
complex = Expresiones algebraicas.

"""

salto = "\n"
espacio = " "

x = 5
y = 13.8
z = (3 + 5j)   # Este es un número complejo.

suma = (x+y+z)
print(f"Valor de suma: {suma}")   # Impresióon por medio de la función format in line.

#mensaje2 = ("El valor de la suma es: ", suma)
#print(salto + mensaje2)

print("\nEl valor de la suma es: " + str(suma))   # Convertir datos en string (str).

# Convención de variables.
mensaje = ("El valor de la suma es: " + str(suma))

print(salto + mensaje)

# Tipos de datos con la función type().
print(salto + "El tipo de dato de x es: "  + str(type(x)))
print(salto +"El tipo de dato de y es: "  + str(type(y)))
print(salto +"El tipo de dato de z es: "  + str(type(z)))
print(salto +"El tipo de dato de suma es: "  + str(type(suma)))

mensaje = ("El valor de la suma es: " + str(suma))
print(salto + mensaje)

print(salto + "* ----------------------------------------------------------------- *")
# Tipos de operadores.
# Operadores aritméticos.
"""
+  = suma
-  = resta
*  = multiplicaciíon
/  = División
%  = Residuo de división.
"""
r = (5+2)
print(f"{salto}{r}")   # Suma.
r = (5-2)
print(f"{salto}{r}")   # Resta.
r = (5*2)
print(f"{salto}{r}")   # Multiplicación
r = (5/2)
print(f"{salto}{r}")   # División
r = (5%2)
print(f"{salto}{r}")   # Módulo.
r = (5**2) 
print(f"{salto}{r}")   # Potencia.
r = (5//2)
print(f"{salto}{r}")   # División entera.

palabra = "uno"
palabra2 = "dos"

print(palabra + espacio + palabra2)
print(palabra * 3)

num = float(input("Dame un número: "))

