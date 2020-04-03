from Colores import Colors


def determinarTam():
    tamaño = int(input("\n\nDe qué tamaño quieres el tablero ? (3 en ralla, 4 en ralla, etc): "))

    while tamaño < 3:
        tamaño = int(input("\nMe tienes que dar un tamaño mayor o igual a 3: "))

    return tamaño

    # Obliga al usuario a escoger un tamaño de tablero válido


def escogeLetra():
    letra = input("\n\n\nQuieres jugar con la X o con 0 ?:  ")

    while letra.upper() != "X" and letra != "0":
        letra = input("\nMe tienes que dar una X o 0 (un cero):  ")

    letraOrdenador = "0" if letra.upper() == "X" else "X"

    return letra.upper(), letraOrdenador

    # Obliga al usuario a escoger una letra válida y a partir de ella determina la del Ordenador


def quienEmpieza():
    print("\n\n\nQuién empieza, tú o el ordenador?", end=" ")
    Colors.green()
    Colors.bold()
    empieza = input(("(TÚ = 1 | ORDENADOR = 2): "))
    Colors.reset()

    while empieza != "1" and empieza != "2":
        print("\nMe tienes que dar un Uno o un Dos", end=" ")
        Colors.green()
        Colors.bold()
        empieza = input("(TÚ = 1 | ORDENADOR = 2):  ")
        Colors.reset()

    return empieza

    # Obliga al usuario a elegir si empieza el ordenador o él mismo


def chooseOption():
    opcion = int(input("\n\n\nPara comenzar el juego dame 1, para acabar el programa dame 0, (COMENZAR = 1 | ACABAR = 0):  "))

    while opcion != 1 and opcion != 0:
        opcion = int(input("\nIntenta de nuevo, (COMENZAR = 1 | ACABAR = 0):  "))

    return opcion

    # Obliga a elegir una opción válida, continuar o parar
