import os
import time
from funciones.mostrar_menu import mostrar_menu
from funciones.buscar_palabra import buscar_palabra
# from funciones.agregar_palabra import agregar_palabra
# from funciones.eliminar_palabra import eliminar_palabra
# from funciones.eliminar_palabra import eliminar_palabra
# from funciones.reemplazar_palabra import reemplazar_palabra
# from funciones.contar_palabras import contar_palabras
# from funciones.contar_oraciones import contar_oraciones
# from funciones.contar_parrafos import contar_parrafos


# Función Interface Principal
def iniciar_programa():
    pagina_libro = input('Por favor, ingrese el texto de la pagina del libro: ')

    continuar = True
    while continuar:
        opcion = mostrar_menu()

        if opcion == 8:
            print("Saliendo del programa...")
            time.sleep(2)
            os.system('cls')
            break

        if opcion == 1:
            # Implementar búsqueda de palabra
            buscar_palabra(pagina_libro)
        elif opcion == 2:
            # Implementar agregar palabra
            print("Función de agregar palabra todavía no está desarrollada.")
        elif opcion == 3:
            # Implementar eliminar palabra
            print("Función de eliminar palabra todavía no está desarrollada.")
        elif opcion == 4:
            # Implementar reemplazar palabra
            print("Función de reemplazar palabra todavía no está desarrollada.")
        elif opcion == 5:
            # Implementar contar palabras
            print("Función de contar palabras todavía no está desarrollada.")
        elif opcion == 6:
            # Implementar contar oraciones
            print("Función de contar oraciones todavía no está desarrollada.")
        elif opcion == 7:
            # Implementar contar párrafos
            print("Función de contar párrafos todavía no está desarrollada.")
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")
        

        # Preguntar al usuario si quiere continuar
        print('')
        respuesta = input("¿Desea realizar otra operación? (s/n): ").lower()
        if respuesta == 's':
            os.system('cls')
        else:
            continuar = False
            print("Saliendo del programa...")
            time.sleep(2)  # Esperar 2 segundos antes de salir
            os.system('cls')


# Iniciar el programa
iniciar_programa()
