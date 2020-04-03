from Funciones.Matriz import crearMatriz
from Colores.Colors import bold, reset, red, cyan


class Tablero:

    def __init__(self, tamaño):
        self.tablero = crearMatriz(tamaño, tamaño)

        # Crea un tablero de las dimensioanes introducidas por el usuario

    def escribir(self, letra, fila, columna):
        if self.tablero[fila][columna] != "*":
            return False

        else:
            self.tablero[fila][columna] = letra
            reset()
            return True

        # Escribe en el tablero lo que quiere el usuario, solo si la casilla a escribir no está ocupada

    def mostrar(self):
        print("\n\n\nEl tablero es: \n\n")

        for fila in self.tablero:
            bold()
            for elemento in fila:
                print(elemento, end="    ")
            print("\n")
        reset()

        # Muestra el tablero tal como esta despues de las jugadas, sin colores

    def mostrarConColores(self, letraUsuario, letraOrdenador):
        print("\n\n\nEl tablero es: \n\n")

        for fila in self.tablero:
            for elemento in fila:

                if elemento == letraUsuario:
                    bold()
                    cyan()
                    print(elemento, end="    ")
                    reset()

                elif elemento == letraOrdenador:
                    bold()
                    red()
                    print(elemento, end="    ")
                    reset()

                else:
                    bold()
                    print(elemento, end="    ")
                    reset()

            print("\n")

        # Muestra el tablero tal como está después de las jugadas, con colores. No puede mostrar el tablero vacío

    # Las siguientes funciones cubren todos los posibles casos de Tres en Ralla:

    # TRES EN RALLA POR FILAS

    def esTresRallaPorFilas(self):

        for fila in self.tablero:
            esTresRalla = True

            for elemento in fila:
                if elemento != fila[0] or elemento == '*':
                    esTresRalla = False
                    break

            if esTresRalla:
                break

        return esTresRalla

    # TRES EN RALLA POR COLUMNAS

    def esTresRallaPorColumnas(self):

        for columna in range(len(self.tablero)):
            esTresRalla = True

            for elemento in range(len(self.tablero)):

                if self.tablero[elemento][columna] != self.tablero[0][columna] or self.tablero[elemento][columna] == '*':
                    esTresRalla = False
                    break

            if esTresRalla:
                break

        return esTresRalla

    # TRES EN RALLA POR DIAGONAL PRINCIPAL

    def esTresRallaPorDiagonalPrincipal(self):

        esTresRalla = True

        for i in range(len(self.tablero)):
            if self.tablero[i][i] != self.tablero[0][0] or self.tablero[i][i] == '*':
                esTresRalla = False
                break

        return esTresRalla

    # TRES EN RALLA POR DIAGONAL SECUNDARIA

    def esTresRallaPorDiagonalSecundaria(self):

        esTresRalla = True
        recorreReves = -1

        for fila in self.tablero:
            if fila[recorreReves] != self.tablero[0][-1] or fila[recorreReves] == '*':
                esTresRalla = False
                break

            recorreReves -= 1

        return esTresRalla

    # La siguiente función comprueba si tenemos un tres en ralla o no haciendo uso de las 4 anteriores

    def tenemosTresRalla(self):
        return self.esTresRallaPorFilas() or self.esTresRallaPorColumnas() or self.esTresRallaPorDiagonalPrincipal() or self.esTresRallaPorDiagonalSecundaria()

    def tableroLleno(self):
        for fila in self.tablero:
            for elemento in fila:
                if elemento == '*':
                    return False

        return True

        # Comprueba si el tablero está lleno
