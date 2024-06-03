# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Buscar palabra (buscar la primera ocurrencia y posición a partir de la palabra y posición dada.)")
    print("2. Agregar palabra (a partir de una posición dada)")
    print("3. Eliminar palabra (a partir de una posición dada)")
    print("4. Reemplazar palabra (a partir de la posición dada)")
    print("5. Contar palabras (cantidad de palabras encontradas en un texto)")
    print("6. Contar oraciones (cantidad de oraciones encontradas en un texto)")
    print("7. Contar párrafos (cantidad de párrafos encontrados en el texto)")
    print("8. Salir")
    return int(input("Ingrese una opcion: "))