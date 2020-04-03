from Clases.Tablero import Tablero
from Clases.Usuario import User

from Funciones.Menu import chooseOption, determinarTam, quienEmpieza, escogeLetra
from Funciones.Jugadas import jugadaUsuario, jugadaOrdenador, gameEnd, ganaUsuario, ganaOrdenador

from Colores.Colors import green, cyan, bold, reset


# Pedimos el nombre

bold()
print("Dime tu nombre de usuario: ", end="")
cyan()
userName = input()
reset()

# Creamos un objeto de la clase User

newUser = User(userName)

# Iniciamos el juego

opcion = chooseOption()

# Inicializamos las variables que se corresponden a los datos del jugador

numPartidas = 1
ganadas = 0
perdidas = 0
empates = 0

# Bucle para saber si continuamos el juego o paramos

while opcion != 0:

    green()
    bold()
    print("\n\n\nPARTIDA", numPartidas)
    reset()

    # Condiciones Iniciales

    dimensionTab = determinarTam()
    tablero = Tablero(dimensionTab)

    tablero.mostrar()

    primerJugador = quienEmpieza()
    letraUsuario, letraOrdenador = escogeLetra()

    # Empieza el usuario

    if primerJugador == "1":

        while True:

            # Comprobamos si el movimiento del usuario ha finalizado la partida

            jugadaUsuario(tablero, letraUsuario, letraOrdenador)
            if gameEnd(tablero):
                if ganaUsuario(tablero, letraUsuario) is None:
                    empates += 1
                else:
                    ganadas += 1

                break

            # Comprobamos si el movimiento del ordenador ha finalzado la partida

            jugadaOrdenador(tablero, letraUsuario, letraOrdenador)
            if gameEnd(tablero):
                if ganaOrdenador(tablero, letraOrdenador) is None:
                    empates += 1
                else:
                    perdidas += 1

                break

    # Empieza el ordenador

    else:

        while True:

            # Comprobamos si el movimiento del ordenador ha finalzado la partida

            jugadaOrdenador(tablero, letraUsuario, letraOrdenador)
            if gameEnd(tablero):
                if ganaOrdenador(tablero, letraOrdenador) is None:
                    empates += 1
                else:
                    perdidas += 1

                break

            # Comprobamos si el movimiento del usuario ha finalizado la partida

            jugadaUsuario(tablero, letraUsuario, letraOrdenador)
            if gameEnd(tablero):
                if ganaUsuario(tablero, letraUsuario) is None:
                    empates += 1
                else:
                    ganadas += 1

                break

    # Final de la partida

    newUser.actualizar(numPartidas, ganadas, perdidas, empates)

    bold()
    print("\n\n\nTus Datos Actuales son los siguientes: \n")

    for key, value in newUser.usuario.items():
        bold()
        print("\t", key, ":", end=" ")
        cyan()
        print(value)
        reset()

    reset()

    numPartidas += 1

    opcion = chooseOption()
