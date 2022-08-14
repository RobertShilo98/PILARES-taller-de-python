"""
Autor: Roberto Jaime Rico Sandoval.
Fille: Ejercicio 1 / Práctica 6
Date: 12/ 06/ 2022
Folio: 964NB09
"""

class Personas():

    def __init__(self, nombre, edad, dni):

        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def setDni(self, dni):
        self.nombre = dni

    def getDni(self):
        return self.dni

    def mostrar(self):

        return print(f"\nLa persona se llama: {self.nombre}\nLa persona tiene: {self.edad}\nDNI de la persona: {self.dni}")

    def esMayorDeEdad(self):

        eva = True

        if self.edad >= 18:
            return print(f"\n{self.nombre}: ¿Es mayor de edad?  -  {eva}")
        else:
            return print(f"\n{self.nombre}: ¿Es mayor de edad?  -  {not(eva)}")
    

Persona1 = Personas("Roberto Sandoval", 12, 169024)
print(Persona1.mostrar())
print(Persona1.esMayorDeEdad())

