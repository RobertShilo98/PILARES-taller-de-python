"""
Autor: Roberto Jaime Rico Sandoval.
Folio: 964NB09
Date: 18/ 08/ 2022
Fille: colección de palabras.
"""

import random

def diccionarios():
    
    estados = ["Cdmx", "Edomex", "Bajacalifornia", "Bajacaliforniasur", "Aguascalientes",
        "Campeche", "Chiapas", "Chihuahua", "Coahuila", "Colima", "Durango", "Guanajuato",
        "Guerrero", "Hidalgo", "Jalisco", "Michoacan", "Morelos", "Nayarit", "Nuevoleon",
        "Oaxaca", "Puebla", "Queretaro", "Quintanaroo", "Sanluispotosi", "Sinaloa",
        "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz", "Yucatan", "Zacatecas"]

    clave = random.choice(estados)
    
    return clave


def words():

    return diccionarios()

