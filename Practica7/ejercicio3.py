"""
Autor: Roberto Jaime Rico Sandoval.
Fille: Ejercicio 2 / Práctica 6
Date: 12/ 06/ 2022
Folio: 964NB09
"""

import random

class Cuenta():

    def __init__(self, titular = "User", cantidad = 0.0):
        self.titular = titular
        self._cantidad = cantidad

    def setTitular(self, titular):
        self.titular = titular

    def getTitular(self):
        return self.titular

    def setTitular(self, cantidad):
        self._cantidad = cantidad

    def getCantidad(self):
        return self._cantidad

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

edad = int(input("\n\n*** Bienvenido al sistema de cuenta jóven ***\n¿Cuantos años tienes?  -  "))

class cuentaJoven(Cuenta):

    def __init__(self, titular="User", cantidad=0.0, bonificacion=0.2):
        Cuenta.__init__(self, titular, cantidad)
        self.bonificacion = bonificacion

    def setBonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def getBonificacion(self):
        return self.bonificacion

    def titularValido(self):
        
        eva = True

        if edad >= 18 and edad <= 25:
            print(f"\nEl titular de la cuenta es valido, es mayor de edad: {edad}\n{eva}")
            print(f"\n¿Deseas retirar dinero?\n1) sí\n2) No")

            re = int(input("\n\nRespuesta:  "))

            while re < 1 or re > 2:
                print(f"\nDato erroneo {re}. vuelve a intentarlo.")
                print(f"\n¿Deseas retirar dinero?\n1) sí\n2) No")

                re = int(input("\n\nRespuesta:  "))

            if re == 1:
                print(f"Estado de cuenta: ${estudiante._cantidad}")
                estudiante.retirar()
            elif re == 2:
                print(f"\nSaliendo del sistema, hasta luego {estudiante.titular}")

        else:
            print(f"El titular es invalido, es menor de edad o supera los 25 años: [{edad}\n{not(eva)}]")

    def mostrarCuentaJoven(self):

        if edad >= 18 and edad <= 25:

            self.bonificacion = random.uniform(0.02, 0.09)
            neto = (round(self.bonificacion,3) * self._cantidad)

            total = (neto + self._cantidad)

            rentabilidad = round(estudiante.bonificacion * 100,1)

            print(f"\nLa rentabilidad de la bonificación para la cuenta de {estudiante.titular} es de: {rentabilidad}%")

            print(f"\n ** Datos de la cuenta **\n\nTitular: {self.titular}\nEstado de la cuenta bruto: ${self._cantidad}\nEstado de la cuenta neto: ${total}")

        else:
            print(f"\n ** Datos de la cuenta **\n\nTitular: {self.titular}\nEstado de la cuenta bruto: ${self._cantidad}")


estudiante = cuentaJoven("Samuel Faret", 2500)

estudiante.titularValido()

estudiante.mostrarCuentaJoven()

