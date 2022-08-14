"""
Autor: Roberto Jaime Rico Sandoval.
Fille: Herencía en POO.
Date: 10/ 08/ 2022
"""

num = 1

class Persona():
    
    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad

class Empleado(Persona):
    
    
    def __init__(self, nombre, genero, edad, empresa):
        Persona.__init__(self, nombre, genero, edad)
        self.empresa = empresa    
    
    def obtenerDatosUsuario(self):
        return self.nombre, self.genero, self.edad, self.empresa
    
class Supervisor(Empleado):
    
    def __init__(self, nombre, genero, edad, empresa, departamento):
        Empleado.__init__(self, nombre, genero, edad, empresa)
        self.departamento = departamento
        
    def obtenerDatosSV(self):
        return self.nombre, self.genero, self.edad, self.empresa, self.departamento 

Empleado1 = Empleado("Roberto Sandoval", "M", 24, "Micronet")
print(f"Datos del empleado 1: {Empleado1.obtenerDatosUsuario()}")

Supervisor1 = Supervisor("Fernado Sandoval", "M", 32, "Micronet", "Sistemas")
print(f"Datos del supervisor 1: {Supervisor1.obtenerDatosSV()}")

#print(f"\nNombre del SV: {Supervisor1.nombre}\nGénero del SV: {Supervisor1.genero}\nEdad del SV: {Supervisor1.edad}\nDepartamento perteneciente SV: {Supervisor1.departamento}")
