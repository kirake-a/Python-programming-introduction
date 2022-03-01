'''
Repite la ejecucion del bloque de codigo para cada elemento de la secuencia "secuencia",
 asignado dicho elemento a "i" en cada repeticion.
 
 Se puede interrumpir en cualquier momento la ejecucion del bloque de codigo con la instruccion
 BREAK, o saltar la ejecucion para un determinado elemento de la secuencia con la instruccion
 CONTINUE.
 
 Usado para recorrer colecciones de objetos como cadenas, listas, tuplas o diccionarios.
 
 Usado a menudo con la instruccion RANGE
 
 1. range(fin): genera una secuencia de numeros enteros desde 0 hasta fin-1
 
 2. range(inicio, fin, salto): Genera una secuencia de numeros enteros desde inicio hasta fin-1
 con un incremento de "salto"
 '''

# Veamos el comportamiento del ciclo For recorriendo a una cadena
palabra = 'Python'

for letra in palabra:
    print(letra)

# Ahora el ciclo For recorrera valores del 1-10 haciendo un santo de 2 entre cada print, 
# en este caso esta imprimiento a los numeros impares ubicados del 1 al 10
for i in range(1, 10, 2):
    print(i, end = ', ')
