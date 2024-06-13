def pedir_texto():
    ingreser_texto = input('Ingrese 1 si desea ingresar un texto, ENTER para texto default: ')
    if ingreser_texto == '1':
        pagina_libro = input('Por favor, ingrese el texto de la pagina del libro: ')
    else:
        pagina_libro = """        Tres anillos para los Reyes Elfos bajo el cielo.
        Siete para los Señores Enanos en casas de piedra.
        Nueve para los Hombres Mortales condenados a morir.
        Uno para el Señor Oscuro, sobre el trono oscuro
        en las Tierras de Mordor, donde se extienden las Sombras.
        Un Anillo para gobernarlos a todos. Un Anillo para encontrarlos,
        Un Anillo para atraerlos a todos y atarlos en las tinieblas
        en la Tierra de Mordor, donde se extienden las Sombras."""
            
    return pagina_libro