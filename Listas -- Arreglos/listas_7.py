"""System module."""
# El fragmento de código genera una lista de diez elementos y
# la rellena con cuadrados de diez números enteros que comienzan
# desde cero (0, 1, 4, 9, 16, 25, 36, 49, 64, 81)
SQUARES = [x ** 2 for x in range(10)]

# Crea un board con 8 filas (iterador j), con 8 elementos en cada
# una de las filas (iterador i), con la palabra "EMPTY"
# dentro de cada casilla
board = [["EMPTY" for i in range(8)] for j in range(8)]
