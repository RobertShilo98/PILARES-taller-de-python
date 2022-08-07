"""
Autor: Roberto Jaime Rico Sandoval
Fille: POO métodos constructores / Disparadores.
Date: 05/ 08/ 2022
Folio: 964NB09

"""

# Definición de clase.
class Perros():

    # Declaración del método constructor.
    def __init__(self, raza, color, tamaño, geografia):
        
        # Definición de atributos.
        self._raza = raza           #Atributo privado.
        self._color = color
        self.tamaño = tamaño        #Atributo público.
        self.geografia = geografia

    """ Método Getter and Setter / Dar y Obtener"""
    def setEdad (self, edad):
        self._edad = edad

    def getEdad (self):
        return self._edad

    def setVacunas(self, vacunas):
        self._vacunas = vacunas

    def getVacunas(self):
        return self._vacunas

        # Atributo protegido.
        # self.__edad = __edad                    

# Declaración de objeto, en clase Perros.
perrosMexicanos = Perros("xoloitzcuintle", "Café obscuro", "Mediano", "México")
print(f"Raza de perro: {perrosMexicanos._raza}\nColor de perro: {perrosMexicanos._color}\nTamaño de perro: {perrosMexicanos.tamaño}\nGeolocalización: {perrosMexicanos.geografia}")

# Accesos de atributo e actualización de dato.
perrosMexicanos._color = "Negro"
print(f"Nuevo color de perro {perrosMexicanos._raza}. Ahora {perrosMexicanos._color}")

# Ingresar y devolver un dato con el método getter and setter.
perrosMexicanos.setEdad(5)
print(f"Edad del perro: {perrosMexicanos.getEdad()}")

perrosMexicanos.setVacunas(True)
print(f"¿El perro está vacunado?: {perrosMexicanos.getVacunas()}")

