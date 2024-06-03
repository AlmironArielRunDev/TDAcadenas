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
