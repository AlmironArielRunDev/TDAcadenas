# Función encontrar palabra
# ------------------------------------------------------------------------------
def buscar_palabra(texto):
    palabra = input("Ingrese la palabra que desea buscar: ")
    posicion_inicial = int(input("Indique la posicion a partir de la cual buscar: "))
    index = texto.find(palabra, posicion_inicial)

    if index != -1:
        print('')
        print(f"La palabra {palabra} comienza en la posición: {index}")
    else:
        print('')
        print(f"La palabra {palabra} no fue encontrada después de la posición {posicion_inicial}.")



# Agregar palabra
# ------------------------------------------------------------------------------
def agregar_palabra(texto):

    palabra = input("Ingrese la palabra que desea agregar: ")
    posicion = int(input("Indique la posicion en la que quiere agregar la palabra: ")) - 1
    
    palabras = texto.split()
    
    while posicion < 0 or posicion > len(palabras):
        raise ValueError("La posición especificada está fuera de los límites del texto.")
        posicion = int(input("Indique la posicion en la que quiere agregar la palabra: ")) - 1
   

    palabras.insert(posicion, palabra)
    texto_modificado = ' '.join(palabras)
    
    print('')
    print("Texto modificado: " , texto_modificado)



# Eliminar palabra
# ------------------------------------------------------------------------------
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
        


# Reemplazar palabra
# ------------------------------------------------------------------------------
def reemplazar_palabra(texto):
    palabra_a_reemplazar = input("Ingrese la palabra que desea reemplazar: ")
    posicion_inicial = int(input("Indique la posición a partir de la cual quiere comenzar a buscar la palabra (1 para el inicio): ")) - 1
    nueva_palabra = input("Ingrese la nueva palabra: ")
    
    palabras = texto.split()
    
    if posicion_inicial < 0 or posicion_inicial >= len(palabras):
        raise ValueError("La posición especificada está fuera de los límites del texto.")
    
    palabra_reemplazada = False
    for i in range(posicion_inicial, len(palabras)):
        if palabras[i] == palabra_a_reemplazar:
            palabras[i] = nueva_palabra
            palabra_reemplazada = True
            break
    
    if not palabra_reemplazada:
        print("No se encontró la palabra a reemplazar a partir de la posición especificada.")
        return
    
    texto_modificado = ' '.join(palabras)
    
    print('')
    print("Texto modificado: ", texto_modificado)




# Contar Palabras
# ------------------------------------------------------------------------------
def contar_palabras(texto):
    palabras = texto.split()
    
    cantidad_palabras = len(palabras)
    
    return print(f"La página de libro ingresada contiene {cantidad_palabras} palabras.")



# Contar Oraciones
# ------------------------------------------------------------------------------
def contar_oraciones(texto):
    # Lista de los signos que indican cuando termina una frase u oración
    signos = ['.', '?', '!']
    
    contar_oraciones = 0
    
    for caracter in texto:
        if caracter in signos:
            contar_oraciones += 1
    # Si el texto finaliza y no hay punto
    if texto[-1] not in signos:
        contar_oraciones += 1
        
    return print(f"la página de libro ingresada está comformada por {contar_oraciones} oraciones.")




# Contar Parrafos
# ------------------------------------------------------------------------------
def contar_parrafos(texto):
    contador_parrafos = 0
    dentro_de_parrafo = False

    for i in range(len(texto)):
        if texto[i] != '\n':
            dentro_de_parrafo = True
        elif texto[i] == '\n' and (i + 1 < len(texto) and texto[i + 1] == '\n'):
            if dentro_de_parrafo:
                contador_parrafos += 1
                dentro_de_parrafo = False
            i += 1  # Saltar el siguiente \n
        elif texto[i] == '\n' and (i + 1 >= len(texto) or texto[i + 1] != '\n'):
            if dentro_de_parrafo and i + 1 >= len(texto):
                contador_parrafos += 1
                dentro_de_parrafo = False

    if dentro_de_parrafo:
        contador_parrafos += 1

    return print(f"El texto proporcionado contiene {contador_parrafos} párrafos")
