"""
Autor: Roberto Jaime Rico Sandoval.
Fille: Ejercicio 2 / Práctica 6
Date: 12/ 06/ 2022
Folio: 964NB09
"""

class Cuenta():

    def __init__(self, titular = "User", cantidad = 0.0, edad = 18):
        self.titular = titular
        self._cantidad = cantidad
        self.edad = edad

    def setTitular(self, titular):
        self.titular = titular

    def getTitular(self):
        return self.titular

    def setTitular(self, cantidad):
        self._cantidad = cantidad

    def getCantidad(self):
        return self._cantidad

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad
        

    def mostrar(self):
        return print(f"\nTitular: {self.titular}\nEstado de la cuenta: ${self._cantidad}")

    def ingresar(self):
        
        deposito = float(input("\n¿Cuánto dinero deseas depositar?  -  $"))

        if deposito > 0:
            self._cantidad += deposito
            return print(f"Estado de cuenta: ${self._cantidad}")
        elif deposito <= 0:
            pass


    def retirar(self):
        
        retiro = float(input("\n¿Cuánto dinero deseas retirar?  -  "))

        while retiro <= 0:
            print(f"\n\nDato erroneo: ${retiro}. Vuelve a intentarlo")
            retiro = float(input("\n¿Cuánto dinero deseas retirar?  -  $"))

        if retiro <= self._cantidad:
            return print(f"\nOperación satisfactoria.\nEstado de cuenta: ${(self._cantidad - retiro)}")
        elif retiro > self._cantidad:
            return print(f"\nOperación invalida. Saldo insuficiente.\nEstado de cuenta: ${self._cantidad}")

cuenta1 = Cuenta("Joaquín Gúzman", 2100)

cuenta1.mostrar()
cuenta1.ingresar()
cuenta1.retirar()
