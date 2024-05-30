# Función encontrar palabra
def buscar_palabra(texto):
    palabra = input("Ingrese la palabra que desea buscar: ")
    posicion_inicial = int(input("Indique la posicion a partir de la cual buscar: "))
    index = texto.find(palabra, posicion_inicial)

    if index != -1:
        print(f"La palabra {palabra} comienza en la posición: {index}")
    else:
        print(f"La palabra {palabra} no fue encontrada después de la posición {posicion_inicial}.")
