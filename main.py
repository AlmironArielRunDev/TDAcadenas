import os
import time
from funciones.mostrar_menu import mostrar_menu
from tda.tda_cadenas import buscar_palabra, agregar_palabra, eliminar_palabra, reemplazar_palabra, contar_palabras, contar_oraciones, contar_parrafos



# Función Interface Principal
def iniciar_programa():
    pagina_libro = input('Por favor, ingrese el texto de la pagina del libro: ')
    
    continuar = True
    while continuar:
        opcion = mostrar_menu()

        if opcion == 8:
            print("Saliendo del programa...")
            time.sleep(1)
            os.system('cls')
            break

        if opcion == 1:
            # Implementar búsqueda de palabra
            buscar_palabra(pagina_libro)
        elif opcion == 2:
            # Implementar agregar palabra
           agregar_palabra(pagina_libro)
        elif opcion == 3:
            # Implementar eliminar palabra
            eliminar_palabra(pagina_libro)
        elif opcion == 4:
            # Implementar reemplazar palabra
            reemplazar_palabra(pagina_libro)
        elif opcion == 5:
            # Implementar contar palabras
            contar_palabras(pagina_libro)
        elif opcion == 6:
            # Implementar contar oraciones
            contar_oraciones(pagina_libro)
        elif opcion == 7:
            # Implementar contar párrafos
            contar_parrafos(pagina_libro)
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
            time.sleep(1)  # Esperar 2 segundos antes de salir
            os.system('cls')


# Iniciar el programa
iniciar_programa()
