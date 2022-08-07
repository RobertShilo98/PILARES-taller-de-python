"""
Autor: Roberto Jaime Rico Sandoval
Fille: Tercer ejercicio de la práctica 4
Date: 04/ 08/ 2022
Folio: 964NB09

"""
fin = 5
num = 1
suma = 0

mini = maxi = 1

registro = []


for ca in range(fin):

    calificacion = float(input(f"Calificación {num}: "))
    num += 1

    mini = calificacion

    if calificacion > maxi:
        maxi = calificacion

    if mini < calificacion:
        mini = calificacion

    registro.append(calificacion)
    suma += calificacion

print(f"\nCalificaciones ingresadas: {registro}")

promedio = (suma/fin)
print(f"\nPromedio general / media: {promedio}")

print(f"\nValor máximo en función predeterminada: {max(registro)}")

print(f"\nValor mínimo en función predeterminada: {min(registro)}")

print(f"\nValor máximo en iteración: {maxi}")

print(f"\nValor mínimo en iteración: {mini}")

