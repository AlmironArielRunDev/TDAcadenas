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