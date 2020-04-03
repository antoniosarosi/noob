def crearMatriz(filas, columnas):
    matriz = []
    for i in range(filas):
        elemento = ["*"] * columnas
        matriz.append(elemento)

    return matriz

# Crea una matriz de los tamaños que recibe, que nos sirve de tablero
