def eliminar_palabra(texto):

    palabra = input("Ingrese la palabra que desea eliminar: ")
    posicion_inicial = int(input("Indique la posicion a partir de la cual buscar: "))
    index = texto.find(palabra, posicion_inicial)

        # Si la palabra se encuentra, eliminarla
    if index != -1:
        # Calcular la longitud de la palabra
        longitud_palabra = len(palabra)
        # Eliminar la palabra del texto
        texto_actualizado = texto[:index] + texto[index + longitud_palabra:]
        print(texto_actualizado)
    else:
        print("La palabra especificada no se encontró en el texto.")
        



