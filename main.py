import os
import time
from funciones.funciones_interface import mostrar_menu, pedir_texto
from funciones.validaciones import validar_reingreso
from tda.tda_cadenas import (
    buscar_palabra, agregar_palabra, eliminar_palabra,
    reemplazar_palabra, contar_palabras, contar_oraciones, contar_parrafos
)


# Función Interface Principal
def iniciar_programa():
    pagina_libro = pedir_texto()

    os.system('cls')

    ejecutar = True
    while ejecutar:
        opcion = mostrar_menu(pagina_libro)

        match opcion:
            case 9:
                print("Saliendo del programa...")
                time.sleep(1)
                os.system('cls')
                break
            case 1:
                buscar_palabra(pagina_libro)
            case 2:
                pagina_libro = agregar_palabra(pagina_libro)
            case 3:
                pagina_libro = eliminar_palabra(pagina_libro)
            case 4:
                pagina_libro = reemplazar_palabra(pagina_libro)
            case 5:
                contar_palabras(pagina_libro)
            case 6:
                contar_oraciones(pagina_libro)
            case 7:
                contar_parrafos(pagina_libro)
            case 8:
                os.system('cls')
                pagina_libro = pedir_texto()
                continue  # Volver al inicio del ciclo sin preguntar por continuar
            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")

        # Preguntar al usuario si quiere continuar realizando operaciones
        print('')
        respuesta = input("¿Desea realizar otra operación? (s/n): ").lower()
        respuesta = validar_reingreso(respuesta)
        if respuesta == 's':
            os.system('cls')
        else:
            ejecutar = False
            print("Saliendo del programa...")
            time.sleep(1)  # Esperar 1 segundo antes de salir
            os.system('cls')


iniciar_programa()
