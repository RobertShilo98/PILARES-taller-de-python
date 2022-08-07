"""
Autor: Roberto Jaime Rico Sandoval
Fille: Colecciones de datos.
Date: 26/ 07/ 2022
Folio: 964NB09

"""

listaNumerica = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"lista numérica: {listaNumerica}")

# Rango de lista.
sublista = listaNumerica[2:5]
print(f"\nSublista numérica: {sublista}")

# Salto de índice.
sublista2 = listaNumerica[1:8:2]
print(f"\nSublista numérica: {sublista2}")

# Concatenación de listas.
sublista3 = listaNumerica[1: :2] + [12, 14]    # Lista con fin predefinido.
print(f"\nSublista numérica: {sublista3}")

# Contar total de datos en la lista (Función predeterminada).
print(f"\n{len(listaNumerica)}")

# Encontrar un valor en la lista (Función predeterminada).
print(f"\n{4 in listaNumerica}")

listaNumerica.append(15)
print(f"lista numérica: {listaNumerica}")

""" -----------------------------------------------------------------------------------------  """

# Tuplas #
colores = ("Vede", "Dojo", "Azud", "Amadillo", "Modado")    # Definición de tupla.
print(f"\n{colores}")

# Acceder a un valor por índice.
print(f"\nColor P3: {colores[4]}")

""" -----------------------------------------------------------------------------------------  """

# Diccionarios #
# Clave:Valor #

edad = {
    "Juan":35,
    "Ana":23,
    "Pedro":40,
    "Bodoque":24
}

print("\nJuanito tiene: " + str(edad["Juan"]))

