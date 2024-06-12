#  Función que valida, que el valor ingresado sea entero
def validar_int(opcion):
    loop = True
    while loop:
        try:
            opcion = int(opcion)
            loop = False
        except ValueError:
            print("\n\tERROR. Debe ingresar sólo valores ENTEROS.")
            opcion = input("\n\tIngrese nuevamente una opción: ")
            loop = True
    return opcion

#  Función que valida, que el valor ingresado pertenezca a un rango de valores que estará determinado por las variables start y end
def validar_rango(opcion, start, end):
    while opcion < start or opcion > end:
        print("\nERROR. Debe ingresar sólo valores VÁLIDOS.")
        print("\nLos valores deben estar comprendidos entre", start, "y", end, "para considerarse una opción válida.")
        opcion = input("\nIngrese nuevamente una opción: ")
        opcion = validar_int(opcion)
    return opcion

#  Función que valida el reingreso al bucle del main
def validar_reingreso(opcion):
    opciones = ["s","n"]
    while opcion not in opciones:
        print("\nERROR. Debe ingresar una opcion valida (s / n)")
        opcion = input("¿Desea realizar otra operación? (s/n): ").lower()