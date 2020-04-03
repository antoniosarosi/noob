"""
El paquete Funciones contiene los siguientes modulos:

    * Matriz
    * Menu
    * Jugadas

Estos modulos contienen las siguiente funciones:

--------------------------------------------------------------------------------------------------------------------------

* Matriz

    ** crearMatriz(filas, columnas)

        Recibe como parametros el numero de filas y de columnas y devuelve una matriz de esas dimensiones cuyos elementos
        son asteriscos (*), es decir crea un tablero vacíoself.

--------------------------------------------------------------------------------------------------------------------------

* Menu

    ** determinarTam()

        No recibe parámetros, le pide al usuario de qué tamaño quiere el tablero, que tiene que ser minimo de 3, y devuelve
        ese número


    ** escogeLetra()

        No recibe parámetros, obliga al usuario a escoger entre X o 0, y una vez el usuario ha elegido una letra válida
        asigna la otra al Ordenador, y devuelve dos variables letraUsuario y letraOrdenador que contienen lo que su
        nombre indica


    ** quienEmpieza()

        No recibe parámetros, obliga al usuario a elegir entre 1 y 2, siendo uno que comienza el usuario como primer
        jugador y dos lo mismo para el ordenador, devuelve mediante la variable empieza el número que ha elegido el
        usuario

    ** chooseOption()

        Simplemente devuelve 1 o 2 según lo que escoja el usuario, que nos servirá en Main.py para saber si el usuario
        quiere continuar o parar

--------------------------------------------------------------------------------------------------------------------------

* Jugadas

    ** computerData(tablero)

        Haciendo uso de la funcion randint de la biblioteca random asigna a las variables fila y columna valores validos
        para escribir en el tablero y las devuelve


    ** computerMove(tablero, letra)

        Usa la funcion anterior para escribir en el tablero la letra que se le pasa como parametro (la del ordenador)


    ** playerData(tablero)

        Recibe una matriz cuadrada como parámetro (el tablero) y devuelve la fila y columna donde quiere escribir el
        usuario. Hay que tener en cuenta que a la hora de pedir datos al usuario los elementos de la matriz (filas)
        empiezan en uno, pero al devolverlos se devuelven restandoles uno, ya que en realidad los elementos de listas
        empiezan en 0


    ** playerMove(tablero, letra)

        Recibe un objeto tablero y una letra como parametro (la letra escogida anteriormente por el usuario) y escribe
        esa letra en el tablero, en la posicion indicada por el usuario a traves de la funcion playerData()


    ** jugadaUsuario(tablero, letraUsuario, letraOrdenador)

        Recibe el objeto tablero y las letras, y escribe en pantalla la ultima jugada realizada por el usuario


    ** jugadaOrdenador(tablero, letraUsuario, letraOrdenador)

        Es igual que la funcion anterior pero muestra por pantalla la jugada realizada por el ordeandor


    ** gameEnd(tablero)

        Comprueba si el juego ha acabado (ya sea por tres en ralla o tablero lleno). Devuelve True si ha acabado,
        False si no. Recibe el objeto tablero


    ** ganador(tablero, letra)

        Si hay una letra que ha creado un tres en ralla, la devuelve. Si no, si el tablero está lleno devuelve 0.
        Si no ocurre nada de esto devuelve None


    ** ganaUsuario(tablero, letraUsuario)

        Hace uso de la función anterior para determinar si el usuario ha ganado o si hay empate Escribe por pantalla
        qué opción ha ocurrido y devuelve 0 si el usuario ha ganado, None si hay empate


    ** ganaOrdenador(tablero, letraOrdenador)

        Es igual que la anterior, pero para el ordenador

--------------------------------------------------------------------------------------------------------------------------
"""


"""
El paquete Clases contiene los modulos:

    * Tablero
    * Usuario

Los cuales contienen:

--------------------------------------------------------------------------------------------------------------------------

* Tablero

    ** __init__(self, tamaño)

        Constructor de la clase Tablero, crea haciendo uso de crearMatriz() un tablero vacio del tamaño que recibe como
        parametro


    ** escribir(self, letra, fila, columna)

        Escribe en el tablero la letra que se le pasa como parámetro en la fila y columna también pasadas como parámetro.
        Si ha podido escribir, devuelve True, si no (porque la casilla está ocupada) devuelve False


    ** mostrar(self)

        Simplemente saca el tablero por pantalla


    ** mostrarConColores(self, letraUsuario, letraOrdenador)

        Saca el tablero por pantalla colorenado con colores distintos las letras del usuario y del ordenador, que las
        tiene que recibir como parámetros


    ** esTresRallaPorFilas(self):

        Devuelve True si hay un tres en ralla en una fila, False si no


    ** esTresRallaPorColumnas(self)

        Lo mismo para columnas


    ** esTresRallaPorDiagonalPrincipal(self)

        Lo mismo para la diagonal principal


    ** esTresRallaPorDiagonalSecundaria(self)

        Lo mismo para la segunda diagonal


    ** tenemosTresRalla(self)

        Devuelve True si hay un tres en ralla de cualquier tipo, false si no. Usa las 4 funciones anteriores


    ** tableroLleno(self)

        Si el tablero está lleno, devuelve True, si no False

--------------------------------------------------------------------------------------------------------------------------

* Usuario

    ** __init__(self, nombre)

        Constructor de la clase User, crea un diccionario que contiene datos del usuario


    ** actualizar(self, partidasTotales, partidasGanadas, partidasPerdidas, empates)

        Actualiza el diccionario creado en el constructor

--------------------------------------------------------------------------------------------------------------------------
"""


"""
El paquete Colores solo contiene el modulo Colors, que contiene:

    red(), green(), cyan(), blue() las cuales a partir del momento en que se llaman, todo lo que salga en pantalla por un
    print o input sera del color indicado

    bold() una vez se llama todo lo siguiente que salga en pantalla será negrita

    reset() todo lo que salga en pantalla a partir de aqui sera de color y estilo normal
"""
