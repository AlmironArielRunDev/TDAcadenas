from funciones.validaciones import validar_int, validar_rango
from funciones.split_casero import split_casero

# Función buscar palabra
# ------------------------------------------------------------------------------
def buscar_palabra(texto):
    palabras = split_casero(texto)
    palabra = input("Ingrese la palabra que desea buscar: ")
    posicion_inicial = input("Indique la posición a partir de la cual buscar: ")
    posicion_inicial = validar_int(posicion_inicial)
    
    # Convertir la posición de palabra a posición de lista restandole 1
    # para que el usuario se guie por numero posicion de palabra 
    posicion_inicial -= 1

    # Verificar si la posición inicial es válida
    if posicion_inicial < 0 or posicion_inicial >= len(palabras):
        print("La posición inicial especificada no es válida.")
        return

    # Buscar la palabra en la lista de palabras
    index = -1
    for i in range(posicion_inicial, len(palabras)):
        if palabras[i] == palabra:
            index = i
            break

    if index != -1:
        print('')
        print(f"La palabra '{palabra}' comienza en la posición: {index + 1}") 
    else:
        print('')
        print(f"La palabra '{palabra}' no fue encontrada después de la posición {posicion_inicial + 1}.")




# Agregar palabra
# ------------------------------------------------------------------------------
def agregar_palabra(texto):

    palabra = input("Ingrese la palabra que desea agregar: ")
    posicion = input("Indique la posicion en la que quiere agregar la palabra: ")
    posicion = validar_int(posicion)
    
    palabras = split_casero(texto)
    
    while posicion < 0 or posicion > len(palabras):
        print(f"Valor fuera de rango, ingrese un numero valido. (entre 0 y {len(palabras)})")
        posicion = int(input("Indique la posicion en la que quiere agregar la palabra: "))
        
    palabras.insert(posicion, palabra)  
    texto_modificado = " ".join(palabras)
    print("Texto modificado:\n" , texto_modificado)
    
    
# Eliminar palabra
# ------------------------------------------------------------------------------
def eliminar_palabra(texto):
    palabra = input("Ingrese la palabra que desea eliminar: ")
    posicion_inicial = input("Indique la posición a partir de la cual buscar: ")
    posicion_inicial = validar_int(posicion_inicial)
    
    # Dividir el texto en palabras
    palabras = split_casero(texto)

    # Validar que la posición inicial esté dentro del rango del texto
    if not (1 <= posicion_inicial <= len(palabras)):
        print("La posición inicial especificada está fuera de los límites del texto.")
        return

    # Ajustar la posición inicial para que coincida con el índice de lista (restar 1)
    posicion_inicial -= 1

    # Recorrer las palabras y eliminar la primera aparición de la palabra especificada
    for i in range(len(palabras)):
        if i >= posicion_inicial and palabras[i] == palabra:
            del palabras[i]
            break

    # Unir las palabras nuevamente en un texto actualizado
    texto_actualizado = ' '.join(palabras)
    print(texto_actualizado)



# Reemplazar palabra
# ------------------------------------------------------------------------------
def reemplazar_palabra(texto):
    palabra_a_reemplazar = input("Ingrese la palabra que desea reemplazar: ")
    nueva_palabra = input("Ingrese la nueva palabra: ")
    posicion_inicial = int(input("Indique la posición a partir de la cual buscar: "))
    
    # Dividir el texto en palabras
    palabras = split_casero(texto)

    # Validar que la posición inicial esté dentro del rango del texto
    if not (1 <= posicion_inicial <= len(palabras)):
        print("La posición inicial especificada está fuera de los límites del texto.")
        return

    # Ajustar la posición inicial para que coincida con el índice de lista (restar 1)
    posicion_inicial -= 1

    # Recorrer las palabras y encontrar la primera aparición de la palabra a reemplazar
    for i in range(len(palabras)):
        if i >= posicion_inicial and palabras[i] == palabra_a_reemplazar:
            palabras[i] = nueva_palabra
            break

    # Unir las palabras nuevamente en un texto actualizado
    texto_actualizado = ' '.join(palabras)
    print(texto_actualizado)




# Contar Palabras
# ------------------------------------------------------------------------------
def contar_palabras(texto):
    palabras = split_casero(texto)
    
    cantidad_palabras = len(palabras)
    
    return print(f"La página de libro ingresada contiene {cantidad_palabras} palabras.")



# Contar Oraciones
# ------------------------------------------------------------------------------
def contar_oraciones(texto):
    # Lista de los signos que indican cuando termina una frase u oración
    signos = ['.']
    
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
    # Dividir el texto en líneas
    lineas = texto.split('\n')

    # Contar los párrafos
    parrafos = 0
    en_parrafo = False

    for linea in lineas:
        if linea.strip():  # Si la línea no está vacía
            if not en_parrafo:
                parrafos += 1
                en_parrafo = True
        else:
            en_parrafo = False

    return print(f"Número de párrafos: {parrafos}")

