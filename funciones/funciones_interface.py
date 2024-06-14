from funciones.validaciones import validar_int, validar_rango
# Función para mostrar el menú de opciones
def mostrar_menu(texto):
    print(texto)
    print('')
    print("Menú de opciones:")
    print("1. Buscar palabra (buscar la primera ocurrencia y posición de la palabra y posición dada.)")
    print("2. Agregar palabra (a partir de una posición dada)")
    print("3. Eliminar palabra (a partir de una posición dada)")
    print("4. Reemplazar palabra (a partir de la posición dada)")
    print("5. Contar palabras (cantidad de palabras encontradas en un texto)")
    print("6. Contar oraciones (cantidad de oraciones encontradas en un texto)")
    print("7. Contar párrafos (cantidad de párrafos encontrados en el texto)")
    print("8. Ingresar nuevo texto")
    print("9. Salir")
    print("")
    opcion = input("Ingrese una opcion: ")
    opcion = validar_int(opcion)
    opcion = validar_rango(opcion,1,9)
    return opcion


# Funcion para pedir un texto al usuario o usar el default
def pedir_texto():
    opcion = input('Ingrese 1 si desea ingresar un texto, ENTER para texto default: ')
    if opcion == '1':
        pagina_libro = input('Por favor, ingrese el texto de la pagina del libro: ')
    else:
        pagina_libro = """        Tres anillos para los Reyes Elfos bajo el cielo.
        Siete para los Señores Enanos en casas de piedra.
        Nueve para los Hombres Mortales condenados a morir.
        Uno para el Señor Oscuro, sobre el trono oscuro
        en las Tierras de Mordor, donde se extienden las Sombras.
        Un Anillo para gobernarlos a todos. Un Anillo para encontrarlos,
        Un Anillo para atraerlos a todos y atarlos en las tinieblas
        en la Tierra de Mordor, donde se extienden las Sombras."""
            
    return pagina_libro