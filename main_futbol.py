# main_futbol.py

from equipo_futbol import cargar_matriz, mostrar_matriz, modificar_matriz

def menu():
    matriz = []
    while True:
        print("\n📋 Menú Principal")
        print("1. Pedir datos para cargar la matriz")
        print("2. Mostrar matriz")
        print("3. Modificar matriz")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            matriz = cargar_matriz()
        elif opcion == "2":
            if matriz:
                mostrar_matriz(matriz)
            else:
                print("La matriz aún no fue cargada.")
        elif opcion == "3":
            if matriz:
                modificar_matriz(matriz)
            else:
                print("Primero debe cargar la matriz.")
        elif opcion == "4":
            print("Programa finalizado.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

menu()
