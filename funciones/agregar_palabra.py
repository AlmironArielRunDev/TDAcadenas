def agregar_palabra(texto):

    palabra = input("Ingrese la palabra que desea agregar: ")
    posicion = int(input("Indique la posicion en la que quiere agregar la palabra: ")) - 1
    
    palabras = texto.split()
    
    while posicion < 0 or posicion > len(palabras):
        raise ValueError("La posición especificada está fuera de los límites del texto.")
        posicion = int(input("Indique la posicion en la que quiere agregar la palabra: ")) - 1
   

    palabras.insert(posicion, palabra)
    texto_modificado = ' '.join(palabras)
    
    print("Texto modificado: " , texto_modificado)
