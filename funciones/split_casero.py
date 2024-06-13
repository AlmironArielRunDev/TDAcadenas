def split_casero(texto):
    palabras = []
    palabra = ''
    
    for caracter in texto:
        if caracter == ' ':  # Espacio indica fin de palabra
            if palabra:
                palabras.append(palabra)
                palabra = ''
        else:
            palabra += caracter
    
    # Añadir la última palabra si existe
    if palabra:
        palabras.append(palabra)
    
    return palabras
