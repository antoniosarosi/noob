class User:

    def __init__(self, nombre):
        self.usuario = {'Nombre': nombre, 'Partidas Jugadas': 0, 'Partidas Ganadas': 0, 'Partidas Perdidas': 0, 'Empates': 0}


    def actualizar(self, partidasTotales, partidasGanadas, partidasPerdidas, empates):
        self.usuario.update({'Partidas Jugadas': partidasTotales,
                             'Partidas Ganadas': partidasGanadas,
                             'Partidas Perdidas': partidasPerdidas,
                             'Empates': empates})

# usuario es simplemente un diccionario que contiene el nombre de quien está jugando y sus partidas ganadas y perdidas.
# El metodo actualizar evidentemente actualiza todos los datos del usuario.
