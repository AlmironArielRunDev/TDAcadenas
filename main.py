import os
import time
from funciones.mostrar_menu import mostrar_menu
from funciones.validaciones import validar_reingreso
from tda.tda_cadenas import buscar_palabra, agregar_palabra, eliminar_palabra, reemplazar_palabra, contar_palabras, contar_oraciones, contar_parrafos



# Función Interface Principal
def iniciar_programa():
    pagina_libro = input('Por favor, ingrese el texto de la pagina del libro: ')
    os.system('cls')
    
    continuar = True
    while continuar:
        opcion = mostrar_menu(pagina_libro)

        match opcion:
            case 8:
                print("Saliendo del programa...")
                time.sleep(1)
                os.system('cls')
                break

            case 1:
                buscar_palabra(pagina_libro)
            case 2:
                agregar_palabra(pagina_libro)
            case 3:
                eliminar_palabra(pagina_libro)
            case 4:
                reemplazar_palabra(pagina_libro)
            case 5:
                contar_palabras(pagina_libro)
            case 6:
                contar_oraciones(pagina_libro)
            case 7:
                contar_parrafos(pagina_libro)
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 8.")
        

        # Preguntar al usuario si quiere continuar realizando operaciones
        print('')
        respuesta = input("¿Desea realizar otra operación? (s/n): ").lower()
        respuesta = validar_reingreso(respuesta)
        if respuesta == 's':
            os.system('cls')
        else:
            continuar = False
            print("Saliendo del programa...")
            time.sleep(1)  # Esperar 2 segundos antes de salir
            os.system('cls')


iniciar_programa()
