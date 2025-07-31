peliculas = ["Los juegos del hambre", "El club de la pelea", "El gran truco", 
             "Gladiador", "Tiempos violentos"]

categorias = {
    "Los juegos del hambre": "Mejor película de Acción",
    "El club de la pelea": "Mejor Guion",
    "El gran truco": "Mejor Guion",
    "Gladiador": "Mejor Drama",
    "Tiempos violentos": "Mejor Drama"}

votos = {
    "Los juegos del hambre": 0,
    "El club de la pelea": 0,
    "El gran truco": 0,
    "Gladiador": 0,
    "Tiempos violentos": 0}

def ganadores():
    print("Peliculas ganadoras por categoría:")

    for categoria in set(categorias.values()):
        mayor = 0
        ganador = []
        for voto in peliculas:
            if categorias[voto] == categoria:
                if votos[voto] > mayor:
                    mayor = votos[voto]
                    ganador = [voto]
                elif votos[voto] == mayor:
                    ganador.append(voto)
        if len(ganador) == 1:
            print(f"{categoria}: {ganador[0]} con {mayor} votos")


while True:
    print("Películas nominadas:")
    for nombre, categoria in categorias.items():
        print(f"- {nombre} ({categoria})")

    try:
        voto = input("\nEscriva el nombre de la pelicula que desea votar (o escriba 'salir' para terminar): ")

        if voto.lower() == "salir":
            break
        if voto not in peliculas:
            raise ValueError("Película no válida.")

        votos[voto] += 1

        print("Voto emitido con exito")
    except:
        print("Entrada inválida. Intente nuevamente.")

print("\nGracias por participar en las nominacion a las mejores peliculas\n")

ganadores()
