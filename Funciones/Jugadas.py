from Colores import Colors

from random import randint


# ORDENADOR

def computerData(tablero):
    fila = randint(0, len(tablero.tablero) - 1)
    columna = randint(0, len(tablero.tablero) - 1)

    return fila, columna

    # Genera números random para la fila y columna entre 0 y lo que valga el length de tablero (no incluido)


def computerMove(tablero, letra):
    fila, columna = computerData(tablero)
    move = tablero.escribir(letra, fila, columna)

    while move is False:
        fila, columna = computerData(tablero)
        move = tablero.escribir(letra, fila, columna)

    return fila, columna

    # Obliga al ordenador a escribir en una posicion valida del tablero


# JUGADOR HUMANO

def playerData(tablero):
    fila = int(input("\nEn qué fila quieres escribir?  "))

    while fila < 1 or fila > len(tablero):
        fila = int(input("NO VÁLIDO. En qué fila quieres escribir?  "))

    columna = int(input("\nEn qué columna quieres escribir?  "))

    while columna < 1 or columna > len(tablero):
        columna = int(input("NO VÁLIDO. En qué columna quieres escribir?  "))

    return fila - 1, columna - 1

    # Obliga al usuario a escoger posiciones y letras válidas y las devuelve.
    # Recibe directamente la matriz tablero, que no el objeto tablero.


def playerMove(tablero, letra):
    fila, columna = playerData(tablero.tablero)
    move = tablero.escribir(letra, fila, columna)

    while move is False:
        print("\nCasilla OCUPADA")
        fila, columna = playerData(tablero.tablero)
        move = tablero.escribir(letra, fila, columna)

    return fila + 1, columna + 1

    # Con ayuda de playerData() obliga al usuario a escribir en posiciones que no estan ocupadas


# Los siguientes dos procedimientos realizan los movimientos llamando a las funciones anteriores y los sacan por pantalla

def jugadaUsuario(tablero, letraUsuario, letraOrdenador):
    fila, columna = playerMove(tablero, letraUsuario)

    tablero.mostrarConColores(letraUsuario, letraOrdenador)

    print("Tu jugada ha sido:", end=" ")

    Colors.cyan()
    Colors.bold()

    print(letraUsuario, end=" ")

    Colors.reset()

    print("en la fila", fila, "y columna", columna)

    # Movimiento del usuario


def jugadaOrdenador(tablero, letraUsuario, letraOrdenador):
    fila, columna = computerMove(tablero, letraOrdenador)

    tablero.mostrarConColores(letraUsuario, letraOrdenador)

    print("La jugada del ordenador ha sido:", end=" ")

    Colors.red()
    Colors.bold()

    print(letraOrdenador, end=" ")

    Colors.reset()

    print("en la fila", fila + 1, "y columna", columna + 1, "\n\n")

    # Movimiento del ordenador


# Las siguientes funciones nos sirven para acabar el juego y declarar al ganador

def gameEnd(tablero):
    return tablero.tenemosTresRalla() or tablero.tableroLleno()

    # True si hay tres en ralla o tablero lleno, False si no hay ninguna


def ganador(tablero, letra):
    if tablero.tenemosTresRalla():
        return letra

    elif tablero.tableroLleno():
        return 0

    else:
        return None

    # None si no ha pasado nada, 0 si el tablero está lleno(empate), y si hay tres en ralla devuelve la letra que lo ha creado


def ganaUsuario(tablero, letraUsuario):
    if ganador(tablero, letraUsuario) == letraUsuario:
        Colors.cyan()
        Colors.bold()
        print("\n\nHAS GANADO")
        Colors.reset()

        return 0

    elif ganador(tablero, letraUsuario) == 0:
        Colors.bold()
        print("\nNo ha ganado nadie, tenemos un EMPATE")
        Colors.reset()

        return None

    # Comprobamos mediante ganador() si el usuario ha ganado o no


def ganaOrdenador(tablero, letraOrdenador):
    if ganador(tablero, letraOrdenador) == letraOrdenador:
        Colors.red()
        Colors.bold()
        print("\n\nGANA EL ORDENADOR")
        Colors.reset()

        return 0

    elif ganador(tablero, letraOrdenador) == 0:
        Colors.bold()
        print("\nNo ha ganado nadie, tenemos un EMPATE")
        Colors.reset()

        return None

    # Comprobamos mediante ganador() si el ordenador ha ganado
