"""
Autor: Roberto Jaime Rico Sandoval
Fille: Primer ejercicio práctica 6.
Date: 06/ 08/ 2022
Folio: 964NB09

"""

menu = True

libros = {
    "Aura" : "Carlos Fuentes",
    "El señor de los anillos" : "J. R. R. Tolkien",
    "Pedro paramo" : "Juan Rulfo",
    "Clean code" : "Robert C. Martin"
}

musica = {
    "Darius" : "Eléctronica - funk",
    "Technicolor Fabrics" : "Rock indie en español",
    "Tuxedo" : "Pop eléctronico moderno",
    "Far Caspian" : "Rock Indie en inglés",
    "Eptos" : "Rap mexicano",
    "Solo cadaver" : "Rap mexicano",

}

peliculas = {
    "Humpday" : "Lynn Shelton",
    "Ojos bien cerrados" : "Stanley Kubrick",
    "La pasión de cristo" : "Mel Gibson",
    "The Plague Dogs" : "Martin Rosen",
    "Beasts of No Nation" : "Cary Joji Fukunaga",
    "Dont Loock Up" : "Adam McKay"

}

series = {
    "Better Call Saul" : "Vince Gilligan y Peter Gould",
    "Las cosas por limpiar" : "Molly Smith Metzler",
    "Silicon Valley" : "Mike Judge",
    "The Witcher" : " Lauren Schmidt Hissrich",
    "Historia de un crimen: Colosio" : "Jorge A. Jiménez,Ilse Salas,Alberto Guerra",
    "This Is Us" : "Dan Fogelman"

}


print(f"\nSelecciona lo que quieres ver en nestro catálogo.\n1) Recomendaciones de libros.\n2) Recomendaciones de música.\n3) Recomendaciones de peliculas.\n4) Recomendaciones de series.")
print("\nDigita 5 para salir del ménu.")


while menu != 5:
    menu = int(input("Elige que quieres hacer  -  "))

    if menu == 1:
        print("\nHaz elegido nuestro sección de recomendaciones de libros.\n")

        for productos in libros:
            autor = libros[productos]
            print(f"\n{productos} - de {autor}")

    elif menu == 2:
        print("\nHaz elegido nuestro sección de recomendaciones de música.\n")

        for productos in musica:
            genero = musica[productos]
            print(f"\n{productos} - genero {genero}")
    
    elif menu == 3:
        print("\nHaz elegido nuestro sección de recomendaciones de películas.\n")

        for productos in peliculas:
            director = peliculas[productos]
            print(f"\n{productos} - de {director}")

    elif menu == 4:
        print("\nHaz elegido nuestro sección de recomendaciones de series.\n")

        for productos in series:
            director = series[productos]
            print(f"\n{productos} - de {director}")

    elif menu <= 0 or menu > 5:
        print(f"\nError, dato no encontrado {menu}")
        print(f"\nSelecciona lo que quieres ver en nestro catálogo.\n1) Recomendaciones de libros.\n2) Recomendaciones de música.\n3) Recomendaciones de peliculas.\n4) Recomendaciones de series.")
        print("\nDigita 5 para salir del ménu.")

print ("\nHasta la proxima!")

