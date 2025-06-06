def cargar_matriz():
    matriz = []
    for i in range(11):
        jugador = []
        print(f"\nJugador {i+1}:")
        nombre = input("Nombre: ")
        edad = input("Edad: ")
        posicion = input("Posición: ")
        apellido = input("Apellido: ")
        goles = input("Goles en el torneo: ")
        jugador.extend([nombre, edad, posicion, apellido, goles])
        matriz.append(jugador)
    return matriz

def mostrar_matriz(matriz):
    print("\nInformación de los jugadores:")
    print("Fila | Nombre | Edad | Posición | Apellido | Goles")
    for i, jugador in enumerate(matriz):
        print(f"{i+1:>4} | " + " | ".join(jugador))

def modificar_matriz(matriz):
    mostrar_matriz(matriz)
    fila = int(input("\nIngrese la fila del jugador a modificar (1-11): ")) - 1
    columna = int(input("Ingrese la columna a modificar (0=Nombre, 1=Edad, 2=Posición, 3=Apellido, 4=Goles): "))
    nuevo_dato = input("Ingrese el nuevo dato: ")
    matriz[fila][columna] = nuevo_dato
    print("\nDato modificado correctamente.")
